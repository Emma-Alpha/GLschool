from mycelery.main import app
import logging
from django.core.mail import send_mail

log = logging.getLogger("django")


@app.task(name='send_email')
def send_email(from_email, recipient_list, url):
    try:
        send_mail(subject="找回密码", message='', from_email=from_email, recipient_list=recipient_list,
                  html_message='<a href="%s" target="_blank">重置密码</a>' % url)
        return 'ok'
    except:
        log.error("发送邮件失败")
