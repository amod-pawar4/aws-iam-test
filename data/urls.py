from django.urls import path
from .views import ListFilesView, DownloadFileView

urlpatterns = [
    path('list/', ListFilesView.as_view()),
    path('download/<str:filename>/', DownloadFileView.as_view()),
]
