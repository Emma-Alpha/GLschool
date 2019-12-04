from rest_framework import serializers
from .models import Banner


class BannerModelSerializer(serializers.ModelSerializer):
    """学校风景轮播的序列化器"""

    # 序列器声明
    class Meta:
        model = Banner
        fields = ['image', 'link', 'is_http']

