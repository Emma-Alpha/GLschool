from django.urls import path, re_path
from . import views

urlpatterns = [
    path('college/', views.CollegeAPIView.as_view()),  # 学院分类
    path('', views.S_CourseListAPIView.as_view()),  # 首页课程信息
    re_path(r'(?P<pk>\d+)/', views.Course_infoAPIView.as_view()),  # 单个课程详情信息
    path('coursecategory/', views.CourseCategoryAPIView.as_view()),  # 课程分类
    path('detail/', views.CourseLessonAPIView.as_view()),  # 课程详情信息
]
