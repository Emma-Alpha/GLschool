from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from mycelery.email.tasks import send_email
from class_ol_api.libs.geetest import GeetestLib
from rest_framework.response import Response
from django.conf import settings
from django_redis import get_redis_connection
from class_ol_api.settings import constants
import logging
import random
import requests
from rest_framework import status
from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserModelSerializer
from mycelery.sms.tasks import send_sms
from mycelery.email.tasks import send_email
from rest_framework_jwt.settings import api_settings
from itsdangerous import TimedJSONWebSignatureSerializer as TJSS

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
        print("通过第一次验证")
        return Response(response_str)

    def post(self, request):
        """验证码二次验证"""
        challenge = request.data.get(self.gt.FN_CHALLENGE, '')
        validate = request.data.get(self.gt.FN_VALIDATE, '')
        seccode = request.data.get(self.gt.FN_SECCODE, '')
        print(challenge, validate, seccode)
        if self.status:
            result = self.gt.success_validate(challenge, validate, seccode, self.user_id)
        else:
            result = self.gt.failback_validate(challenge, validate, seccode)
        print("result:>>>>>>>>", result)
        result = {"status": "success"} if result else {"status": "fail"}
        return Response(result)


# 腾讯防水墙
aid = '2086788894'
AppSecretKey = '02jW5rcPbPwVmgxwlw3UVIA**'


class VerifyAPIView(APIView):
    def get(self, request):
        # d第一获取验证码
        return Response(aid, status=status.HTTP_200_OK)

    def post(self, request):
        Ticket = request.data.get('ticket')
        Randstr = request.data.get('randstr')
        # 上线后这里要进行修改,改为动态获取请求的ip
        UserIP = '127.0.0.1'

        ret = requests.get('https://ssl.captcha.qq.com/ticket/verify', params={
            'aid': aid,
            'AppSecretKey': AppSecretKey,
            'Ticket': Ticket,
            'Randstr': Randstr,
            'UserIP': UserIP
        })
        dic = ret.json()
        if dic and dic.get('response') == '1':
            return Response('校验成功!', status=status.HTTP_200_OK)
        return Response(dic.get('err_msg'), status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(CreateAPIView):
    """用户注册"""
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


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


class MobileLoginAPIView(APIView):
    # 短信登录
    def post(self, request):
        try:
            mobile = request.data.get("mobile")
            sms = request.data.get("sms")
            user = User.objects.get(mobile=mobile)
            # 连接redis数据库

            redis_conn = get_redis_connection("sms_code")
            sms_code = redis_conn.get("sms_%s" % mobile)
            if sms_code.decode() != sms:
                return Response({"message": "输入的短信有误，请重新输入"}, status.HTTP_404_NOT_FOUND)

            # 使用restframework_jwt模块提供手动生成token的方法生成登录状态
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            user.token = jwt_encode_handler(payload)

            redis_conn.delete("sms_%s" % mobile)
            redis_conn.delete("mobile_%s" % mobile)

        except:
            return Response({"message": "手机号不存在！"}, status.HTTP_404_NOT_FOUND)

        return Response({"token": user.token, "id": user.id, "username": user.username})


class PhoneSetPasswordAPIView(APIView):
    def post(self, request):
        mobile = request.data.get("mobile")
        password = request.data.get("password")
        password2 = request.data.get("password2")
        sms_code = request.data.get("sms_code")

        if not password or not password2:
            return Response("密码不能为空", status=status.HTTP_400_BAD_REQUEST)

        if password2 != password:
            return Response("重置密码失败，两次密码不一致", status=status.HTTP_400_BAD_REQUEST)
        if len(password) < 6 or len(password) > 16:
            return Response("密码的长度应为6-16位之间", status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(mobile=mobile)
        except:
            return Response("充值失败！手机号码不存在！", status=status.HTTP_400_BAD_REQUEST)

        # 连接Redis数据库
        redis_conn = get_redis_connection("sms_code")
        redis_conn_code = redis_conn.get("sms_%s" % mobile).decode()
        print(redis_conn_code, sms_code)
        if redis_conn_code != sms_code:
            return Response("重置密码失败,验证码错误!", status=status.HTTP_400_BAD_REQUEST)

        user.set_password(password)
        user.save()

        redis_conn.delete("sms_%s" % mobile)
        redis_conn.delete("mobile_%s" % mobile)

        return Response('重置密码成功！！！')


# 发送邮件
class SendEmailAPIView(APIView):
    def get(self, request):
        email = request.query_params.get("email")
        # 检测用户是否存在
        try:
            user = User.objects.get(email=email)
        except:
            return Response("邮箱地址错误或不存在", status=status.HTTP_400_BAD_REQUEST)

        # 生成找回密码的连接
        serializer = TJSS(settings.SECRET_KEY, constants.DATA_SIGNATURE_EXPIRE)
        # dumps的返回值是加密数的bytes信息
        access_token = serializer.dumps({"email": email}).decode()

        url = settings.CLIENT_HOST + "/reset_password?access_token=" + access_token

        # 使用django提供的email发送邮件

        send_email(from_email=settings.EMAIL_FROM, recipient_list=[email], url=url)
        print(11111111111)
        send_email.delay(from_email=settings.EMAIL_FROM, recipient_list=["{}".format(email)], url=url)

        return Response("邮件已经发送，请留意您的邮箱")

    def put(self, request):
        access_token = request.data.get("access_token")
        serializer = TJSS(settings.SECRET_KEY, constants.DATA_SIGNATURE_EXPIRE)
        try:
            data = serializer.loads(access_token)
            email = data.get('email')
        except:
            return Response("access_token无效", status=status.HTTP_400_BAD_REQUEST)

        return Response(email)

    def post(self, request):
        access_token = request.data.get("access_token")
        password = request.data.get("password")
        password2 = request.data.get("password2")
        serializer = TJSS(settings.SECRET_KEY, constants.DATA_SIGNATURE_EXPIRE)
        try:
            data = serializer.loads(access_token)
            email = data.get('email')
        except:
            return Response("access_token无效", status=status.HTTP_400_BAD_REQUEST)

        if not password2 or not password:
            return Response("密码不能为空", status=status.HTTP_400_BAD_REQUEST)

        if password2 != password:
            return Response("密码不一致", status=status.HTTP_400_BAD_REQUEST)

        if len(password) < 6 or len(password) > 16:
            return Response("密码的长度应为6-16为之间", status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except:
            return Response("用户邮箱地址不存在", status=status.HTTP_400_BAD_REQUEST)

        user.set_password(password)
        user.save()

        return Response("邮件重置密码成功!!!!")