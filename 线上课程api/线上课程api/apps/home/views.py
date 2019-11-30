from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from .models import Banner, Timer
from .serializers import BannerModelSerializer, TimerModelSerializer
from 线上课程api.settings import constants


# 首页轮播图序列化器
class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_deleted=False).order_by('orders', '-id')[
               :constants.HOME_BANNER_LENGTH]
    serializer_class = BannerModelSerializer


# 热门视频序列化器
class TimerListAPIView(ListAPIView):
    queryset = Timer.objects.filter(is_show=True, is_deleted=False).order_by('orders', '-id')[:constants.HOST_TIMER_IMG]
    serializer_class = TimerModelSerializer


