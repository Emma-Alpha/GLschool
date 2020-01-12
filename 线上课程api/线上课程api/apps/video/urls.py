from django.urls import path
from . import views

urlpatterns = [
    path('host/', views.HostShortVideoAPIView.as_view()),  # 热门短视频
]
