from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from 线上课程api.libs.geetest import GeetestLib
from rest_framework.response import Response
from django.conf import settings

class GeetestCaptchaAPIView(APIView):
    """极验验证码视图类"""
    def __init__(self):
        super().__init__()

        self.gt = GeetestLib(settings.GEETEST["pc_geetest_id"], settings.GEETEST["pc_geetest_key"])
        self.user_id = "test"
        self.status = False

    def get(self,request):
        """获取验证码"""
        self.status = self.gt.pre_process(self.user_id)
        # 将来可以使用redis来保存status和user_id
        response_str = self.gt.get_response_str()
        return Response(response_str)

    def post(self,request):
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

