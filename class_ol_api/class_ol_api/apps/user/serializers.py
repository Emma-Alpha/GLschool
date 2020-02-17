from rest_framework import serializers
from .models import User
from rest_framework.response import Response
from rest_framework import status
from django_redis import get_redis_connection
from django.contrib.auth.hashers import make_password
from rest_framework_jwt.settings import api_settings

import re


class UserModelSerializer(serializers.ModelSerializer):
    """用户序列化器"""
    sms_code = serializers.CharField(write_only=True, max_length=6, min_length=4, help_text="短信验证码")
    token = serializers.CharField(read_only=True, min_length=1, help_text="jwt认证")

    class Meta:
        model = User
        fields = ["id", "username", "token", "password", "mobile", "sms_code"]
        # 字段的额外声明
        extra_kwargs = {
            "id": {"read_only": True},
            "username": {"read_only": True},
            "password": {"write_only": True, "min_length": 6},
            "mobile": {"write_only": True, "min_length": 11},
        }

    def validate(self, attrs):
        """创建用户之前validate"""
        print("attrs>>>>>>>>>>", attrs)
        mobile = attrs.get("mobile")
        sms_code = attrs.get("sms_code")

        # 验证手机号码是否合法
        if not re.match(r"1[3-9]\d{9}$", mobile):
            raise serializers.ValidationError("对不起，手机格式错误！")

        try:
            User.objects.get(mobile=mobile)
            raise serializers.ValidationError("对不起，该手机号已经被注册")



        except User.DoesNotExist:

            # 验证短信是否正确
            redis_conn = get_redis_connection("sms_code")
            real_sms_code = redis_conn.get("sms_%s" % mobile)
            print("real_sms_code>>>>>>>>%s, sms_code>>>>>>>>>>%s" % (real_sms_code, sms_code))

            if real_sms_code.decode() != sms_code:
                raise serializers.ValidationError("对不起，短信验证码错误！本次验证码已失效，请重新发送！")

            # 本次验证以后，直接删除当前本次验证码，防止出现恶意暴力破解
            # 创建管道对象
            pipe = redis_conn.pipeline()
            # 开启事务[无法管理数据库的读取数据操作]
            pipe.multi()
            # 把事务中要完成的所有操作，写入到管道中
            pipe.delete("sms_%s" % mobile)
            pipe.delete("mobile_%s" % mobile)
            # 执行事务
            pipe.execute()

        return attrs

    def create(self, validated_data):
        mobile = validated_data.get("mobile")
        # 对密码进行加密
        password = validated_data.get("password")

        # 对用户名设置一个默认值
        username = mobile

        try:
            user = User.objects.create_user(username=username, password=password, mobile=mobile)
        except:
            raise serializers.ValidationError("用户创建失败")


        # 使用restframework_jwt模块提供手动生成token的方法生成登录状态
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        user.token = jwt_encode_handler(payload)

        return user

