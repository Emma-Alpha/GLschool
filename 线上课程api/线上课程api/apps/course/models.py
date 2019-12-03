from django.db import models
from 线上课程api.utils.models import BaseModel


# Create your models here.
class College(models.Model):
    """学院分类"""
    name = models.CharField(max_length=50, unique=True, verbose_name="学院名称")

    class Meta:
        db_table = 'gl_college'
        verbose_name = "学院名称"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class System(BaseModel):
    """各个系"""
    choice_education = (
        (0,"专科"),
        (1,"本科"),
    )
    name = models.CharField(max_length=50, unique=True, verbose_name="系名称")
    college = models.ForeignKey("College", on_delete=models.CASCADE, related_name="college_system", verbose_name="学院名称")
    education = models.IntegerField(choices=choice_education, default=1,verbose_name="学历")

    class Meta:
        db_table = 'gl_system'
        verbose_name = "系名称"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseCategory(BaseModel):
    """课程分类"""
    name = models.CharField(max_length=50, unique=True, verbose_name="课程名称")
    college = models.ForeignKey("College", on_delete=models.DO_NOTHING, blank=True, null=True,
                                related_name="college_CourseCategory", verbose_name="学院名称")
    system = models.ForeignKey("System", on_delete=models.DO_NOTHING, blank=True, null=True,
                               related_name="system_CourseCategory", verbose_name="系名称")

    class Meta:
        db_table = 'gl_course_category'
        verbose_name = "课程分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Course(BaseModel):
    """实战课程"""
    course_type = (
        (0, '大一'),
        (1, '大二'),
        (2, '大三'),
    )
    level_choices = (
        (0, '初级'),
        (1, '中级'),
        (2, '高级'),
    )
    status_choices = (
        (0, '上线'),
        (1, '下线'),
        (2, '预上线'),
    )
    name = models.CharField(max_length=128, verbose_name="课程名称")
    college = models.ForeignKey('College', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="学院名称",
                                related_name="college_course")
    system = models.ForeignKey("System", on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="系名称",
                               related_name="sysetem_course")
    course_img = models.ImageField(upload_to="course", max_length=255, verbose_name="封面图片", blank=True, null=True)
    course_type = models.SmallIntegerField(choices=course_type, default=0, verbose_name="推荐学习阶段")
    # 使用这个字段的原因
    brief = models.TextField(verbose_name="详情介绍", null=True, blank=True)
    level = models.SmallIntegerField(choices=level_choices, default=1, verbose_name="难度等级")
    pub_date = models.DateField(verbose_name="发布日期", auto_now_add=True)
    period = models.IntegerField(verbose_name="建议学习周期(day)", default=7)
    attachment_path = models.FileField(upload_to="course_attachment", max_length=255, verbose_name="课件路径", blank=True,
                                       null=True)
    status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="课程状态")
    course_category = models.ForeignKey('CourseCategory', on_delete=models.DO_NOTHING, null=True, blank=True,
                                        verbose_name="课程分类")
    students = models.IntegerField(verbose_name="学习人数", default=0)
    lessons = models.IntegerField(verbose_name="总课时数量", default=0)
    pub_lessons = models.IntegerField(verbose_name="课时更新数量", default=0)
    teacher = models.ForeignKey("Teacher", on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="授课老师")

    class Meta:
        db_table = "gl_course"
        verbose_name = "专题课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name


class Teacher(BaseModel):
    """讲师、导师表"""
    role_choices = (
        (0, '老师'),
        (1, '辅导员'),
        (2, '班主任'),
    )
    college = models.ForeignKey("College", on_delete=models.DO_NOTHING, blank=True, null=True,
                                related_name="college_teacher")
    name = models.CharField(max_length=32, verbose_name="名称")
    role = models.SmallIntegerField(choices=role_choices, default=0, verbose_name="职位")
    signature = models.CharField(max_length=255, verbose_name="签名", help_text="签名", blank=True, null=True)
    image = models.ImageField(upload_to="teacher", null=True, blank=True, verbose_name="封面")
    brief = models.TextField(max_length=1024, verbose_name="描述")

    class Meta:
        db_table = "gl_teacher"
        verbose_name = "讲师导师"
        verbose_name_plural = "讲师导师"

    def __str__(self):
        return "%s" % self.name


class CourseChapter(BaseModel):
    """课程章节"""
    course = models.ForeignKey("Course", related_name="course_chapter", on_delete=models.CASCADE, verbose_name="课程名称")
    chapter = models.SmallIntegerField(verbose_name="第几章", default=1)
    name = models.CharField(max_length=128, verbose_name="章节标题")
    summary = models.TextField(verbose_name="章节介绍", blank=True, null=True)
    pub_date = models.DateField(verbose_name="发布日期", auto_now_add=True)

    class Meta:
        db_table = 'gl_course_chapter'
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s:(第%s章)%s" % (self.course, self.chapter, self.name)
