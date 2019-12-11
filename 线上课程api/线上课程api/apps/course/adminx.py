import xadmin
from .models import College


class CollegeModelAdmin(object):
    """学院"""
    pass


xadmin.site.register(College, CollegeModelAdmin)

from .models import Course

from .models import System


class SystemModelAdmin(object):
    """系分类"""
    list_display = ['orders', 'name', 'is_show']


xadmin.site.register(System, SystemModelAdmin)

from .models import CourseCategory


class CourseCategoryModelAdmin(object):
    """课程分类"""
    list_display = ['orders', 'name', 'is_show']


xadmin.site.register(CourseCategory, CourseCategoryModelAdmin)


class CourseModelAdmin(object):
    """课程详情信息"""
    list_display = ['orders', 'name', 'teacher', 'is_show', ]


xadmin.site.register(Course, CourseModelAdmin)

from .models import Teacher


class TeacherModelAdmin(object):
    """老师详情"""
    list_display = ['orders', 'name', 'role']


xadmin.site.register(Teacher, TeacherModelAdmin)

from .models import CourseChapter


class CouresChapterModelAdmin(object):
    """课程章节"""
    list_display = ['orders', 'name', 'is_show']


xadmin.site.register(CourseChapter, CouresChapterModelAdmin)

from .models import CourseLesson


class CourseLessonModelAdmin(object):
    "课时"
    pass


xadmin.site.register(CourseLesson, CourseLessonModelAdmin)
