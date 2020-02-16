from django.urls import path, re_path
from . import views

"""用户自定义上传"""
urlpatterns = [
    path('host/', views.HostShortVideoAPIView.as_view()),  # 热门短视频
    path('upload/', views.UploadVideoAPIView.as_view()),  # 上传视频
    re_path(r'(?P<pk>\d+)/', views.GetVideoInfoAPIView.as_view()),  # 查询某个视频的信息
]
