from django.conf import settings
from urllib.request import urlopen
from urllib.parse import urlencode, parse_qs
import json


class QAuthQQError(Exception):
    pass

class OAuthQQ(object):
    """QQ认证辅助工具"""

    def __init__(self, app_id=None, app_key=None, redirect_uri=None, state=None):
        self.app_id = app_id or settings.QQ_APP_ID
        self.app_key = app_key or settings.QQ_APP_KEY
        self.redirect_url = redirect_uri or settings.QQ_REDIRECT_URL
        self.state = state or settings.QQ_STATE

    def GetAuthorizationCode(self):
        params = {
            "response_type": "code",
            "client_id": self.app_id,
            "redirect_uri": self.redirect_url,
            "state": self.state
        }
        url = "https://graph.qq.com/oauth2.0/authorize?" + urlencode(params)
        return url

    def GetAccessToken(self, code):
        params = {
            "grant_type": "authorization_code",
            "client_id": self.app_id,
            "client_secret": self.app_key,
            "code": code,
            "redirect_uri": self.redirect_url
        }
        url = "https://graph.qq.com/oauth2.0/token?" + urlencode(params)
        try:
            response = urlopen(url)
            response_data = response.read().decode()
            # parse_qs 是将参数
            dic = parse_qs(response_data)
            return dic
        except:
            raise QAuthQQError

    def GetOpenID(self, access_token):
        params = {
            "access_token": access_token
        }
        url = "https://graph.qq.com/oauth2.0/me?" + urlencode(params)
        try:
            response = urlopen(url)
            data = response.read().decode()
            dic = data[10:-3]
            return dic
        except:
            raise QAuthQQError

    def GetUserInfo(self, access_token, openid):
        params = {
            "access_token": access_token,
            "oauth_consumer_key": self.app_id,
            "openid": openid,
        }
        url = "https://graph.qq.com/user/get_user_info?" + urlencode(params)
        try:
            response = urlopen(url)
            user_info_dict = json.loads(response.read().decode())
            return user_info_dict
        except:
            raise QAuthQQError
