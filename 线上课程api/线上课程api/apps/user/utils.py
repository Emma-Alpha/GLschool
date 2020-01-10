def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'token': token,
        'id': user.id,
        'username': user.username
    }


"""实现多条件登录"""
from django.contrib.auth.backends import ModelBackend
from .models import User
from django.db.models import Q


def get_user_by_account(account):
    """通过账号信息获取用户"""
    try:
        user = User.objects.get(Q(username=account) | Q(mobile=account) | Q(email=account))
    except User.DoesNotExist:
        user = None
    return user


class UsernameMobileAuthBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        # 获取用户
        user = get_user_by_account(username)

        # 验证密码和是否允许登录
        if user is not None and user.check_password(password) and self.user_can_authenticate(user):
            return user
