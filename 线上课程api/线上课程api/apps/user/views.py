from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from 线上课程api.libs.geetest import GeetestLib
from rest_framework.response import Response
from django.conf import settings
from django_redis import get_redis_connection
from 线上课程api.settings import constants
from 线上课程api.libs.yuntongxun.sms import CCP
import logging
import random

log = logging.getLogger("django")


# todo 用户登录功能
class GeetestCaptchaAPIView(APIView):
    """极验验证码视图类"""

    def __init__(self):
        super().__init__()

        self.gt = GeetestLib(settings.GEETEST["pc_geetest_id"], settings.GEETEST["pc_geetest_key"])
        self.user_id = "test"
        self.status = False

    def get(self, request):
        """获取验证码"""
        self.status = self.gt.pre_process(self.user_id)
        # 将来可以使用redis来保存status和user_id
        response_str = self.gt.get_response_str()
        return Response(response_str)

    def post(self, request):
        """验证码二次验证"""
        challenge = request.data.get(self.gt.FN_CHALLENGE, '')
        validate = request.data.get(self.gt.FN_VALIDATE, '')
        seccode = request.data.get(self.gt.FN_SECCODE, '')
        if self.status:
            result = self.gt.success_validate(challenge, validate, seccode, self.user_id)
        else:
            result = self.gt.failback_validate(challenge, validate, seccode)
        result = {"status": "success"} if result else {"status": "fail"}
        return Response(result)


from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserModelSerializer
from mycelery.sms.tasks import send_sms

class UserAPIView(CreateAPIView):
    """用户注册"""
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


from rest_framework import status


class MobileAPIView(APIView):
    """验证码手机号码唯一性"""

    # 1. 根据手机号到数据库里面查找用户，返回结果
    def get(self, request, mobile):
        try:
            User.objects.get(mobile=mobile)
            return Response({"status": False})
        except User.DoesNotExist:
            return Response({"status": True})


class SMSAPIView(APIView):
    def get(self, request, mobile):
        """短信发送"""
        # 1. 判断手机号码是否在60秒内曾经发送过短信
        redis_conn = get_redis_connection("sms_code")
        ret = redis_conn.get("mobile_%s" % mobile)
        if ret is not None:
            return Response({"message": "对不起，60秒内已经发送过短信，请耐心等待"})

        # 2. 生成短信验证码
        sms_code = "%06d" % random.randint(1, 999999)

        # 3. 保存短信验证码到redis
        # 创建管道对象
        pipe = redis_conn.pipeline()
        # 开启事务[无法管理数据库的读取数据操作]
        pipe.multi()
        # 把事务中要完成的所有操作，写入到管道中
        pipe.setex("sms_%s" % mobile, constants.SMS_EXPIRE_TIME, sms_code)
        pipe.setex("mobile_%s" % mobile, constants.SMS_INTERVAL_TIME, "_")
        # 执行事务
        pipe.execute()

        # 4. 调用短信sdk,发送短信
        # 调用任务函数，发布任务
        send_sms.delay(mobile, sms_code)

        # 5. 响应发送短信的结果
        return Response({"message": "发送短信成功！"})
