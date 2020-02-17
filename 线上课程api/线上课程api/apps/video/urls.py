from django.urls import path, re_path
from . import views

"""用户自定义上传"""
urlpatterns = [
    path('host/', views.HostShortVideoAPIView.as_view()),  # 热门短视频
    path('upload/', views.UploadVideoAPIView.as_view()),  # 上传视频
    # re_path(r'(?P<pk>\d+)/', views.GetVideoInfoAPIView.as_view()),  # 查询某个视频的信息
    re_path(r'(?P<pk>\d+)/', views.GetVideoInfoAPIView.as_view()),  # 查询短视频中某个视频的信息
    path('image/', views.ShowHomeImageAPIView.as_view()),  # 首页风景轮播图
    path('video_type/', views.VideoTypeAPIView.as_view()),  # 短视频分类
    path('info/', views.ShortVideoAPIView.as_view()),  # 短视频
    path('type/', views.TypeVideoInfoAPIView.as_view()),  # 某个分类下的视频
    path('num/', views.NumVideoAPIView.as_view()),  # 某个分类下的排行榜
]
