from rest_framework import serializers
from .models import College, Course, Teacher, CourseCategory


# 学院分类
class CollegeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('id', 'name',)


# 老师
class TeacherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'name', 'role_list')


# 课程详细页
class CourseModelSerializer(serializers.ModelSerializer):
    college = CollegeModelSerializer()
    teacher = TeacherModelSerializer()

    class Meta:
        model = Course
        fields = (
            'id', 'is_show', 'is_deleted',
            'name', 'college', 'students',
            'brief', 'teacher', 'course_list',
            'is_host', 'course_img',
        )


# 课程分类
class CourseCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['name', 'college', 'system']
