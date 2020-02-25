from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import *
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .paginations import VideoTypeInfoPageNumberPagination
from drf_haystack.viewsets import HaystackViewSet


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
    queryset = Video.objects.all()
    serializer_class = UploadVideoModelSerializer
    permission_classes = [IsAuthenticated]


class GetVideoInfoAPIView(RetrieveAPIView):
    queryset = Video.objects.filter(is_show=True, is_deleted=False, video_status=1)
    serializer_class = UserVideoInfoAllSerializer


class ShowHomeImageAPIView(ListAPIView):
    """首页轮播展示"""
    queryset = HomeVideo.objects.filter(is_show=True, is_deleted=False, is_lunbo=True)
    serializer_class = ShowHomeImageModelSerializer


class VideoTypeAPIView(ListAPIView):
    """视频分类"""
    queryset = VideoType.objects.filter(is_show=True, is_deleted=False)
    serializer_class = VideoTypeModelSerializer


class ShortVideoAPIView(ListAPIView):
    """获取短视频"""

    def get_queryset(self):
        type_id = self.request.GET.get('fenlei')
        queryset = Video.objects.filter(is_show=True, is_deleted=False, video_type=type_id)
        return queryset

    serializer_class = VideoModelSerializer


class TypeVideoInfoAPIView(ListAPIView):
    """获取某个分类视频信息"""

    serializer_class = VideoModelSerializer
    pagination_class = VideoTypeInfoPageNumberPagination

    def get_queryset(self):
        type_id = self.request.GET.get('fenlei')
        queryset = Video.objects.filter(is_show=True, is_deleted=False, video_type=type_id)
        return queryset


class NumVideoAPIView(ListAPIView):
    """排行榜"""
    serializer_class = NumVideoModelSerializer

    def get_queryset(self):
        type_id = self.request.GET.get('fenlei')
        queryset = Video.objects.filter(is_show=True, is_deleted=False, video_type=type_id).order_by("-video_play",'id')
        return queryset


class VideoSearchViewSet(HaystackViewSet):
    """视频搜索"""
    index_models = [Video]

    serializer_class = VideoIndexSerializer