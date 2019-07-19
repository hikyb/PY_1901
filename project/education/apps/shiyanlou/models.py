from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PathCategory(models.Model):
    """路径课程分类"""
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    img = models.ImageField(upload_to="pathcategory_img")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "路径课程分类表"


class PathState(models.Model):
    """路径课程阶段"""
    desc = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name_plural = "路径课程阶段表"


class PathCourse(models.Model):
    """路径课程"""
    title = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    img = models.ImageField(upload_to="path_img")
    category = models.ForeignKey(PathCategory, on_delete=models.CASCADE)
    state = models.ForeignKey(PathState, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "路径课程表"


class PathComment(models.Model):
    """路径课评论"""
    username = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    pathcourse = models.ForeignKey(PathCourse, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "路径课程评论表"


class Category(models.Model):
    """实验课程类别"""
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "实验课程类别表"


class Tags(models.Model):
    """实验课程标签"""
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "实验课程标签表"


class ExperimentCourse(models.Model):
    """实验课程"""
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    focus = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    img = models.ImageField(upload_to="experiment_img")
    vip = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "实验课程表"


class ExperimentList(models.Model):
    """实验课列表类"""
    number = models.IntegerField(default=10)
    list = models.CharField(max_length=20)
    experimentcourse = models.ForeignKey(ExperimentCourse, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.experimentcourse)

    class Meta:
        verbose_name_plural = "实验课程列表表"


class ExperimentComment(models.Model):
    """实验课评论"""
    username = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    experimentcourse = models.ForeignKey(ExperimentCourse, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "实验课程评论表"


class BootcampCourse(models.Model):
    """训练营课程"""
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    recommend = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    focus = models.IntegerField(default=0)
    img = models.ImageField(upload_to="bootcamp_img")
    inform = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "训练营课程表"


class BootcampCourseList(models.Model):
    """训练营课程列表"""
    number = models.IntegerField(default=0)
    title = models.CharField(max_length=20)
    bootcampcourse = models.ForeignKey(BootcampCourse, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "训练营课程表"


class BootcampComment(models.Model):
    """训练营课程评论"""
    username = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    bootcampcourse = models.ForeignKey(BootcampCourse, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "训练营课程评论"


class BootcampInform(models.Model):
    """训练课程实验报告"""
    desc = models.CharField(max_length=200)
    bootcampcourse = models.ForeignKey(BootcampCourse, on_delete=models.CASCADE)

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name_plural = "训练营课程实验报告"


class BootcampAnswer(models.Model):
    """训练课程实验回答"""
    desc = models.CharField(max_length=100)
    bootcampcourse = models.ForeignKey(BootcampCourse, on_delete=models.CASCADE)

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name_plural = "训练营课程实验回答"


class ShiyanlouUser(User):
    user = models.CharField(max_length=20)
    level = models.IntegerField(default=1)
    vip = models.BooleanField(default=False)
    advancevip = models.BooleanField(default=False)
