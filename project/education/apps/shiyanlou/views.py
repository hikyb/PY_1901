from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import *

# Create your views here.


class IndexView(View):
    """首页"""
    def get(self, request):
        # return HttpResponse("首页")
        pathcategory = PathCategory.objects.all()[:6]
        experimentcourse = ExperimentCourse.objects.all()[:4]
        return render(request, 'shiyanlou/index.html', locals())

    # def post(self, request):
    #     print("++++++++")


class CourseView(View):
    """课程页"""
    def get(self, request):
        tags = Tags.objects.all()
        experimentcourse = ExperimentCourse.objects.all()
        return render(request, 'shiyanlou/courses/index.html', locals())


class DeveloperView(View):
    """开发者页面"""
    def get(self, request):
        return render(request, 'shiyanlou/developer/index.html')


class PathsView(View):
    """路径"""
    def get(self, request):
        pathcategory = PathCategory.objects.all()
        return render(request, 'shiyanlou/paths/index.html', locals())


class DiscussionView(View):
    """讨论区"""
    def get(self, request):
        return render(request, 'shiyanlou/questions/index.html')


class DiscussionDetailView(View):
    """讨论区问题详情页"""
    def get(self, request):
        return render(request, 'shiyanlou/questions/show.html')


class BootcampView(View):
    """训练营"""
    def get(self, request):
        bootcampcourse = BootcampCourse.objects.all()
        return render(request, 'shiyanlou/bootcamp/index.html', locals())


class BootcampDeatilView(View):
    """训练营课程详情页"""
    def get(self, request, id):
        bootcampcourse = BootcampCourse.objects.get(pk=id)
        return render(request, 'shiyanlou/courses/show2.html', locals())


class VipView(View):
    """会员"""
    def get(self, request):
        return render(request, 'shiyanlou/vip/index.html')


class PathShowView(View):
    """学习路径详情页"""
    def get(self, request, id):
        pathcategory = PathCategory.objects.get(pk=id)
        pathcourse = PathCategory.objects.get(pk=id).pathcourse_set.all()
        return render(request, 'shiyanlou/paths/show.html', locals())


class CourseShowView(View):
    """课程详情页"""
    def get(self, request, id):
        experimentcourse = ExperimentCourse.objects.get(pk=id)
        experimentcourse.view += 1
        experimentcourse.save()
        return render(request, 'shiyanlou/courses/show.html', locals())


class PrivacyView(View):
    """关于我们"""
    def get(self, request):
        return render(request, 'shiyanlou/privacy/index.html')
