from django.db import models
from 线上课程api.utils.models import BaseModel
from course.models import *


# Create your models here.


class HostShortVideo(BaseModel):
    name = models.CharField(max_length=64, verbose_name="视频名称")
    file_url = models.FileField(null=False, blank=False, verbose_name="视频地址")
    focus_content = models.TextField(null=False, blank=False, verbose_name="焦点内容")
    user_video = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="上传视频所属人")
    course_video = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, verbose_name="视频所属分类")
    video_time = models.CharField(max_length=64, verbose_name="视频时长")

    class Meta:
        db_table = "gl_HostShortVideo"
        verbose_name_plural = verbose_name = "热点短视频"
