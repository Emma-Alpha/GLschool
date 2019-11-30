from django.urls import path
from . import views



urlpatterns = [
    path("banner/", views.BannerListAPIView.as_view()),
    path("timer/", views.TimerListAPIView.as_view()),

]
