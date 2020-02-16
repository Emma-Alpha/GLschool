from rest_framework.views import APIView
from .utils import OAuthQQ
from rest_framework.response import Response
from .models import OAuthUser
from rest_framework import status
from rest_framework_jwt.authentication import api_settings
from itsdangerous import TimedJSONWebSignatureSerializer as TJSS
from django.conf import settings
from user.utils import UsernameMobileAuthBackend
from user.models import User
from django_redis import get_redis_connection
from 线上课程api.settings import constants
import json
import logging

logger = logging.error("django")

# Create your views here.

class QAuthQQAPIView(APIView):
    def get(self, request):
        """
        生成QQ登录的地址
        :param request:
        :return: QQ第三方扫码登录地址
        """
        oauth = OAuthQQ()
        url = oauth.GetAuthorizationCode()
        return Response(url)


class QQInfoAPIView(APIView):
    def get(self, request):
        code = request.query_params.get("code")
        oauth = OAuthQQ()
        many_info = oauth.GetAccessToken(code=code)
        print("many_info>>>>>>>>>>>>>:", many_info)
        access_token = many_info.get("access_token")[0]
        expires_in = many_info.get("expires_in")[0]
        refresh_token = many_info.get("refresh_token")[0]

        if many_info.get("msg"):
            logging.error("code:{}, msg:{}".format(many_info.get("code"), many_info.get("msg")))
            return Response("获取access_token失败", status=status.HTTP_400_BAD_REQUEST)
        # 获取openid
        openid_info = oauth.GetOpenID(access_token=access_token)
        openid_dict = json.loads(openid_info)
        openid = openid_dict.get("openid")
        print('openid', type(openid))
        user_info = oauth.GetUserInfo(access_token=access_token, openid=openid)
        print(user_info)
        try:
            qq_user = OAuthUser.objects.get(openid=openid)
            user = qq_user.user
            # 生成jwt登录token
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            try:
                avatar = user.avatar.url
            except:
                avatar = user_info.get("figureurl_qq_1")

            user_info = {
                "token": token,
                "id": user.id,
                "username": user.username,
                "avatar": avatar,
                "nickname": user_info.get("nickname"),
            }
            return Response({"user_info": user_info, "status": 1})
        except:
            # 没有进行QQ第三方关联
            serializer = TJSS(settings.SECRET_KEY, constants.DATA_SIGNATURE_EXPIRE)
            data = serializer.dumps({'openid': openid, "access_token": access_token, "expires_in": expires_in,
                                     "refresh_token": refresh_token}).decode()
            return Response(
                {"status": 0, "avatar": user_info.get("figureurl_qq_1"), "nickname": user_info.get("nickname"),
                 "data": data})

    def post(self, request):
        d = request.data.get("status")
        try:
            openid = request.data.get("data")

            serializer = TJSS(settings.SECRET_KEY, constants.DATA_SIGNATURE_EXPIRE)
            data = serializer.loads(openid)
            open_id = data.get("openid")
            access_token = data.get("access_token")
            expires_in = data.get("expires_in")
            refresh_token = data.get("refresh_token")

        except:
            return Response("账号绑定超时，请重新登录绑定！", status=status.HTTP_400_BAD_REQUEST)

        # 判断状态码
        if d != 1 and d != 2:
            return Response("QQ登录关联失败！", status=status.HTTP_400_BAD_REQUEST)
        nickname = request.data.get("nickname")
        if d == 1:
            username = request.data.get("count")
            password = request.data.get("password")
            user_avatar = request.data.get("avatar")

            try:
                checkuser = UsernameMobileAuthBackend()
                user = checkuser.authenticate(request, username=username, password=password)
                print(user)
            except:
                return Response("用户不存在！", status=status.HTTP_400_BAD_REQUEST)

            try:
                OAuthUser.objects.create(user_id=user.id, openid=open_id, access_token=access_token,
                                         expires_in=expires_in,
                                         refresh_token=refresh_token)
            except:
                return Response("QQ关联用户失败!", status=status.HTTP_400_BAD_REQUEST)

        if d == 2:
            sms_code = request.data.get("sms_code")
            password = request.data.get("password")
            mobile = request.data.get("mobile")
            user_avatar = request.data.get("avatar")
            try:
                OAuthUser.objects.get(openid=open_id)
                return Response("QQ用户已经绑定另一个用户", status=status.HTTP_400_BAD_REQUEST)
            except:
                pass

            try:
                User.objects.get(mobile=mobile)
                return Response("手机号码已被注册，请重新输入", status=status.HTTP_400_BAD_REQUEST)
            except:
                pass

            try:
                redis_conn = get_redis_connection("sms_code")
                redis_sms_code = redis_conn.get("sms_%s" % mobile).decode()
                if redis_sms_code != sms_code:
                    return Response("验证码错误", status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response('redis数据库连接失败', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            try:
                user = User.objects.create_user(username=mobile, mobile=mobile, password=password)
            except:
                return Response("创建用户失败", status=status.HTTP_400_BAD_REQUEST)

            try:
                OAuthUser.objects.create(user_id=user.id, openid=open_id, access_token=access_token,
                                         expires_in=expires_in,
                                         refresh_token=refresh_token)
            except:
                return Response("关联QQ用户失败", status=status.HTTP_400_BAD_REQUEST)

        # 生成jwt认证
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        try:
            avatar = user.avatar.url
        except:
            avatar = user_avatar

        user_info = {
            "token": token,
            "id": user.id,
            "username": user.username,
            "avatar": avatar,
            "nickname": nickname,
        }
        return Response({"user_info": user_info, "status": 1})