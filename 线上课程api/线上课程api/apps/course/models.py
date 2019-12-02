from django.db import models
from 线上课程api.utils.models import BaseModel


# Create your models here.
class IT_CourseCategory(BaseModel):
    """
    课程分类
    """
    name = models.CharField(max_length=50, unique=True, verbose_name="分类名称")

    class Meta:
        db_table = "gl_it_course_category"
        verbose_name = "信息技术学院课程分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class IT_Course(BaseModel):
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
    course_img = models.ImageField(upload_to="IT_course", max_length=255, verbose_name="封面图片", blank=True, null=True)
    course_type = models.SmallIntegerField(choices=course_type, default=0, verbose_name="推荐学习阶段")
    # 使用这个字段的原因
    brief = models.TextField(verbose_name="详情介绍", null=True, blank=True)
    level = models.SmallIntegerField(choices=level_choices, default=1, verbose_name="难度等级")
    pub_date = models.DateField(verbose_name="发布日期", auto_now_add=True)
    period = models.IntegerField(verbose_name="建议学习周期(day)", default=7)
    attachment_path = models.FileField(upload_to="course_attachment", max_length=255, verbose_name="课件路径", blank=True,
                                       null=True)
    status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="课程状态")
    course_category = models.ForeignKey('IT_CourseCategory', on_delete=models.DO_NOTHING, null=True, blank=True,
                                        verbose_name="课程分类")
    students = models.IntegerField(verbose_name="学习人数", default=0)
    lessons = models.IntegerField(verbose_name="总课时数量", default=0)
    pub_lessons = models.IntegerField(verbose_name="课时更新数量", default=0)
    teacher = models.ForeignKey("IT_Teacher", on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="授课老师")

    class Meta:
        db_table = "gl_it_course"
        verbose_name = "信息技术学院专题课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name


class IT_Teacher(BaseModel):
    """讲师、导师表"""
    role_choices = (
        (0, '讲师'),
        (1, '导师'),
        (2, '班主任'),
    )
    name = models.CharField(max_length=32, verbose_name="讲师title")
    role = models.SmallIntegerField(choices=role_choices,default=0, verbose_name="讲师身份")
    title = models.CharField(max_length=64, verbose_name="职位、职称")
    signature = models.CharField(max_length=255, verbose_name="导师签名", help_text="导师签名", blank=True, null=True)
    image = models.ImageField(upload_to="teacher", null=True, blank=True, verbose_name="讲师封面")
    brief = models.TextField(max_length=1024, verbose_name="讲师描述")

    class Meta:
        db_table = "gl_it_teacher"
        verbose_name = "讲师导师"
        verbose_name_plural = "讲师导师"

    def __str__(self):
        return "%s" % self.name

class IT_CourseChapter(BaseModel):
    """课程章节"""
    course = models.ForeignKey("IT_Course",related_name="IT_coursechapter", on_delete=models.CASCADE, verbose_name="课程名称")
    chapter = models.SmallIntegerField(verbose_name="第几章", default=1)
    name = models.CharField(max_length=128, verbose_name="章节标题")
    summary = models.TextField(verbose_name="章节介绍", blank=True, null=True)
    pub_date = models.DateField(verbose_name="发布日期",auto_now_add=True)

    class Meta:
        db_table = 'gl_it_course_chapter'
        verbose_name = "信息技术学院课程章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s:(第%s章)%s" % (self.course, self.chapter, self.name)

