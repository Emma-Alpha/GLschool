# celery的任务必须写在tasks.py的文件中，别的文件名称不识别!!!
from mycelery.main import app
from class_ol_api.libs.yuntongxun.sms import CCP
from class_ol_api.settings import constants
import logging

log = logging.getLogger("django")

@app.task(name="send_sms")
def send_sms(mobile, sms_code):
    """发送短信"""
    ccp = CCP()
    try:
        ret = ccp.send_template_sms(mobile, [sms_code, constants.SMS_EXPIRE_TIME // 60], constants.SMS_TEMPLATE_ID)
        if ret == -1:
            return "发送短信失败！"
        print("手机号码:{}，发送短信成功".format(mobile))
        return ret
    except:
        log.error("发送短信验证码失败！手机号码{mobile}".format(mobile=mobile))
