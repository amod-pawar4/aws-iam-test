import boto3
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

s3 = boto3.client('s3')

BUCKET1 = "viaq-data"
PREFIX = "device_data/"

class ListFilesView(APIView):
    def get(self, request):
        resp = s3.list_objects_v2(Bucket=BUCKET1, Prefix=PREFIX)
        files = [obj['Key'] for obj in resp.get('Contents', [])]
        return Response({"files": files})

class DownloadFileView(APIView):
    def get(self, request, filename):
        key = f"{PREFIX}{filename}"
        url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': BUCKET1, 'Key': key},
            ExpiresIn=3600
        )
        return Response({"download_url": url})
