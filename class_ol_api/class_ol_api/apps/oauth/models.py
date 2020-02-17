from django.db import models
from user.models import User
from class_ol_api.utils.models import BaseModel


# Create your models here.

class OAuthUser(BaseModel):
    """登录用户数据"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    openid = models.CharField(max_length=64, verbose_name='openid', db_index=True)
    access_token = models.CharField(max_length=64, verbose_name="access_token", db_index=True)
    expires_in = models.CharField(max_length=64, verbose_name="expires_in", db_index=True)
    refresh_token = models.CharField(max_length=64, verbose_name="refresh_token", db_index=True)

    class Meta:
        db_table = 'gl_oauth_qq'
        verbose_name = verbose_name_plural = "QQ登录用户数据"
