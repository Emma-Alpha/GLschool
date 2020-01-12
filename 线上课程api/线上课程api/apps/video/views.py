from django.shortcuts import render
from rest_framework.views import APIView
from .models import HostShortVideo
from rest_framework.response import Response


# Create your views here.
class HostShortVideoAPIView(APIView):
    """热点短视频"""

    def get(self, request):
        """获取某个分类的信息"""
        fenlei = request.query_params.get("fenlei")
        try:
            hsv = HostShortVideo.objects.get(course_video=fenlei)
        except HostShortVideo.DoesNotExist:
            raise Response("分类不存在")
        print(hsv.name, hsv.file_url.url)

        return Response("ok")
