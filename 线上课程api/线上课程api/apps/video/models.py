from django.db import models
from 线上课程api.utils.models import BaseModel
from course.models import *


# Create your models here.


class HostShortVideo(BaseModel):
    POST_STATUS = (
        (0, "未审核"),
        (1, "通过"),
        (2, "不通过"),
    )
    name = models.CharField(max_length=64, verbose_name="视频名称")
    file_url = models.FileField(null=False, blank=False, verbose_name="视频地址")
    focus_content = models.TextField(null=False, blank=False, verbose_name="焦点内容")
    user_video = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="上传视频所属人")
    course_video = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, verbose_name="视频所属分类", default=None)
    video_time = models.CharField(max_length=64, verbose_name="视频时长")
    video_img = models.ImageField(null=False, blank=False, verbose_name="视频封面")
    video_stauts = models.IntegerField(choices=POST_STATUS, default=0, verbose_name="审核状态")

    class Meta:
        db_table = "gl_HostShortVideo"
        verbose_name_plural = verbose_name = "热点短视频"

    @property
    def course(self):
        return self.course_video.name


class VideoType(BaseModel):
    """视频分类"""
    type_name = models.CharField(max_length=64, verbose_name="分类名称")

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = 'gl_VideoType'
        verbose_name_plural = verbose_name = "视频分类"


class Video(BaseModel):
    """视频管理"""
    POST_STATUS = (
        (0, "未审核"),
        (1, "通过"),
        (2, "不通过"),
    )
    name = models.CharField(max_length=64, verbose_name="视频名称")
    file_url = models.FileField(null=False, blank=False, verbose_name="视频地址")
    focus_content = models.TextField(null=False, blank=False, verbose_name="焦点内容")
    user_video = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="上传视频所属人")
    video_type = models.ForeignKey(VideoType, on_delete=models.CASCADE, verbose_name="视频所属分类", default=None)
    video_time = models.CharField(max_length=64, verbose_name="视频时长")
    video_img = models.ImageField(null=False, blank=False, verbose_name="视频封面")
    video_status = models.IntegerField(choices=POST_STATUS, default=0, verbose_name="审核状态")
    video_watch = models.IntegerField(default=0, verbose_name="观看人数")
    video_play = models.IntegerField(default=0, verbose_name="播放次数")

    class Meta:
        db_table = 'gl_Video'
        verbose_name_plural = verbose_name = "视频管理"

    @property
    def video_video_type(self):
        return self.video_type.type_name

    def __str__(self):
        return self.name


class HomeVideo(BaseModel):
    """首页轮播"""
    is_lunbo = models.BooleanField(default=False, verbose_name="是否展示在首页轮播")
    video = models.ForeignKey(Video, on_delete=models.DO_NOTHING, verbose_name="视频")

    class Meta:
        db_table = 'gl_HomeVideo'
        verbose_name_plural = verbose_name = "首页轮播"

    @property
    def video_name(self):
        return self.video.name


class ShortVideo(BaseModel):
    """短视频展示"""
    is_short_show = models.BooleanField(default=False, verbose_name="是否在短视频区域展示")
    video = models.ForeignKey(Video, on_delete=models.DO_NOTHING, verbose_name="视频")

    class Meta:
        db_table = 'gl_ShortVideo'
        verbose_name_plural = verbose_name = "短视频展示"

    @property
    def video_name(self):
        return self.video.name


