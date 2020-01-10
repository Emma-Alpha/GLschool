from django.urls import path
from . import views

urlpatterns = [
    path("QQ_login/", views.QAuthQQAPIView.as_view()),
    path("QQ_info/", views.QQInfoAPIView.as_view()),
]
