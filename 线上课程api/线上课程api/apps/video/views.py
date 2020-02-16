from django.shortcuts import render
from rest_framework.views import APIView
from .models import HostShortVideo
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import HostShortVideoModelSerializer, UploadVideoModelSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class HostShortVideoAPIView(ListAPIView):
    """热点短视频"""

    queryset = HostShortVideo.objects.filter(is_show=True, is_deleted=False, video_stauts=1)
    serializer_class = HostShortVideoModelSerializer

    # def get(self, request):
    #     """获取某个分类的信息"""
    #     fenlei = request.query_params.get("fenlei")
    #     print(fenlei)
    #     try:
    #         hsv = HostShortVideo.objects.get(course_video_id=fenlei)
    #     except HostShortVideo.DoesNotExist:
    #         raise Response("分类不存在")
    #     print(hsv.name, hsv.file_url.url)
    #     info = {
    #         "focus_content": hsv.focus_content,
    #         "name": hsv.name,
    #         "file_url": hsv.file_url.url,
    #         "video_time": hsv.video_time,
    #         "video_img": hsv.video_img.url,
    #     }
    #
    #     return Response(info)


class UploadVideoAPIView(CreateAPIView):
    queryset = HostShortVideo.objects.all()
    serializer_class = UploadVideoModelSerializer
    permission_classes = [IsAuthenticated]
