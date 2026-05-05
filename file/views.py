import boto3
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.conf import settings

s3 = boto3.client('s3')
BUCKET2 = "your-bucket2-name"

class UploadFileView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        file_obj = request.FILES['file']
        key = file_obj.name
        s3.upload_fileobj(file_obj, BUCKET2, key)
        return Response({"message": "File uploaded", "key": key})

class RenameFileView(APIView):
    def post(self, request):
        old_key = request.data['old_key']
        new_key = request.data['new_key']
        s3.copy_object(Bucket=BUCKET2, CopySource={'Bucket': BUCKET2, 'Key': old_key}, Key=new_key)
        s3.delete_object(Bucket=BUCKET2, Key=old_key)
        return Response({"message": "File renamed"})

class DeleteFileView(APIView):
    def delete(self, request, key):
        s3.delete_object(Bucket=BUCKET2, Key=key)
        return Response({"message": "File deleted"})

class ListFilesView(APIView):
    def get(self, request):
        resp = s3.list_objects_v2(Bucket=BUCKET2)
        files = [obj['Key'] for obj in resp.get('Contents', [])]
        return Response({"files": files})

class CreateFolderView(APIView):
    def post(self, request):
        folder_name = request.data['folder_name']
        if not folder_name.endswith('/'):
            folder_name += '/'
        s3.put_object(Bucket=BUCKET2, Key=folder_name)
        return Response({"message": "Folder created", "folder": folder_name})
