# celery的任务必须写在tasks.py的文件中，别的文件名称不识别!!!
from mycelery.main import app
from 线上课程api.libs.yuntongxun.sms import CCP
from 线上课程api.settings import constants
import logging
from rest_framework.response import Response
from rest_framework import status

log = logging.getLogger("django")

@app.task(name="send_sms")
def send_sms(mobile, sms_code):
    """发送短信"""
    ccp = CCP()
    ret = ccp.send_template_sms(mobile, [sms_code, constants.SMS_EXPIRE_TIME // 60], constants.SMS_TEMPLATE_ID)
    if ret == -1:
        return "发送短信失败！"
