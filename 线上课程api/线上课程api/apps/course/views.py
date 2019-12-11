from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .serializers import CollegeModelSerializer, CourseModelSerializer, CourseCategoryModelSerializer, \
    CourseLessonModelSerializer
from .models import College, Course, CourseCategory, CourseLesson
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class CollegeAPIView(ListAPIView):
    """各个学院信息"""
    queryset = College.objects.all()
    serializer_class = CollegeModelSerializer


class S_CourseListAPIView(ListAPIView):
    """首页课程信息"""
    queryset = Course.objects.filter(is_show=True, is_deleted=False).order_by('orders', '-id')
    serializer_class = CourseModelSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ('college',)


class Course_infoAPIView(RetrieveAPIView):
    """课程详情页"""
    queryset = Course.objects.filter(is_show=True, is_deleted=False)
    serializer_class = CourseModelSerializer


class CourseCategoryAPIView(ListAPIView):
    """课程分类"""
    queryset = CourseCategory.objects.filter(is_show=True, is_deleted=False)
    serializer_class = CourseCategoryModelSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ('college',)


class CourseLessonAPIView(ListAPIView):
    """课程详情"""
    queryset = CourseLesson.objects.filter(is_show=True, is_deleted=False)
    serializer_class = CourseLessonModelSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ('course',)
