from django.urls import path
from .views import UploadFileView, RenameFileView, DeleteFileView, ListFilesView, CreateFolderView

urlpatterns = [
    path('upload/', UploadFileView.as_view()),
    path('rename/', RenameFileView.as_view()),
    path('delete/<str:key>/', DeleteFileView.as_view()),
    path('list/', ListFilesView.as_view()),
    path('create-folder/', CreateFolderView.as_view()),
]
