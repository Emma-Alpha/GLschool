import xadmin
from .models import *


class HostShortVideoModelAdmin(object):
    """热门短视频"""
    list_display = ['name', 'video_time', 'video_stauts']


xadmin.site.register(HostShortVideo, HostShortVideoModelAdmin)

