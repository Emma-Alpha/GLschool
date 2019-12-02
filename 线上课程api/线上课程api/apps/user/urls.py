from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('login/mobile/', views.MobileLoginAPIView.as_view()),  # 使用手机号码登录
    re_path(r'login/mobile/(?P<mobile>1[3-9]\d{9})', views.SMSAPIView.as_view()),
    # path('captcha/', views.GeetestCaptchaAPIView.as_view()),
    path('verify/', views.VerifyAPIView.as_view()),  # 腾讯防水墙
    re_path(r"mobile/(?P<mobile>1[3-9]\d{9})/", views.MobileAPIView.as_view()),
    re_path(r"sms/(?P<mobile>1[3-9]\d{9})/", views.SMSAPIView.as_view()),
    path("",views.UserAPIView.as_view()),
]
