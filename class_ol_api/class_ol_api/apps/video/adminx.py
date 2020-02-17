import xadmin
from .models import *


class HostShortVideoModelAdmin(object):
    """热门短视频"""
    list_display = ['name', 'video_time', 'video_stauts']


xadmin.site.register(HostShortVideo, HostShortVideoModelAdmin)


class VideoModelAdmin(object):
    """视频管理"""
    list_display = ['name', 'user_video', 'video_status']


xadmin.site.register(Video, VideoModelAdmin)


class VideoTypeModelAdmin(object):
    """视频分类"""
    list_display = ['type_name']


xadmin.site.register(VideoType, VideoTypeModelAdmin)


class ShortVideoModelAdmin(object):
    """短视频展示"""
    list_display = ['is_short_show', 'video']


xadmin.site.register(ShortVideo, ShortVideoModelAdmin)


class HomeVideoModelAdmin(object):
    """首页轮播"""
    list_display = ['is_lunbo', 'video']


xadmin.site.register(HomeVideo, HomeVideoModelAdmin)
