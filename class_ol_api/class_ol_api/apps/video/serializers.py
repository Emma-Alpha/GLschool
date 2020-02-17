from rest_framework import serializers
from .models import HostShortVideo, ShortVideo, HomeVideo, Video, VideoType
from drf_haystack.serializers import HaystackSerializer
from .search_indexes import VideoIndex


class HostShortVideoModelSerializer(serializers.ModelSerializer):
    """热点短视频"""

    class Meta:
        model = HostShortVideo
        fields = ('id', "video_time", "video_img", "name", "file_url", "focus_content")


class UploadVideoModelSerializer(serializers.ModelSerializer):
    """视频审核记录"""

    class Meta:
        model = HostShortVideo
        fields = ["file_url", "name"]

    def create(self, validate_data):
        """保存数据"""
        user = self.context['request'].user
        print(">>>>>>>>>>>>>.", user)
        print("+++++++++++++", validate_data)
        link = validate_data.get("file_url")
        name = validate_data.get("name")
        print("**********:", name)
        instance = HostShortVideo.objects.create(file_url=link, user_video_id=user.id, name=name)
        # instance.course_video = str(instance.file_url).split('/')[0]
        instance.save()
        return instance


class UserVideoInfoAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostShortVideo
        fields = ('id', "video_time", "video_img", "name", "file_url", "focus_content", 'course')


class VideoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', "video_time", "video_img", "name", "file_url", "focus_content")


class ShowHomeImageModelSerializer(serializers.ModelSerializer):
    video = VideoModelSerializer()
    """首页风景轮播展示"""

    class Meta:
        model = HomeVideo
        fields = ('id', 'video')


class VideoTypeModelSerializer(serializers.ModelSerializer):
    """课程分类"""

    class Meta:
        model = VideoType
        fields = ('id', 'type_name')


class NumVideoModelSerializer(serializers.ModelSerializer):
    """排行榜"""

    class Meta:
        model = Video
        fields = ('id', "video_time", "video_img", "name", "file_url", "focus_content", "video_play")


class VideoIndexSerializer(HaystackSerializer):
    """视频索引结果数据序列化器"""

    class Meta:
        index_classes = [VideoIndex]
        fields = ('text', 'id', 'title', 'focus_content')
