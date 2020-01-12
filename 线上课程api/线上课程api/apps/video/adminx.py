import xadmin
from .models import *


class HostShortVideoModelAdmin(object):
    """学院"""
    pass


xadmin.site.register(HostShortVideo, HostShortVideoModelAdmin)
