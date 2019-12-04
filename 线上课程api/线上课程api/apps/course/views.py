from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .serializers import CollegeModelSerializer, CourseModelSerializer
from .models import College, Course
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
    filter_backends = [DjangoFilterBackend,]
    filter_fields = ('college',)