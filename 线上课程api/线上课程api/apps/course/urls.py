from django.urls import path
from . import views

urlpatterns = [
    path('college/', views.CollegeAPIView.as_view()),   # 学院分类
    path('', views.S_CourseListAPIView.as_view()),  # 课程信息
]
