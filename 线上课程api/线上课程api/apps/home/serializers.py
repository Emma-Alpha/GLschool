from rest_framework import serializers
from .models import Banner, Timer


class BannerModelSerializer(serializers.ModelSerializer):
    """学校风景轮播的序列化器"""

    # 序列器声明
    class Meta:
        model = Banner
        fields = ['image', 'link', 'is_http']


class TimerModelSerializer(serializers.ModelSerializer):
    """热门视频的序列化器"""

    # 序列化器声明
    class Meta:
        model = Timer
        fields = ['image', 'link', 'is_http', 'title']
