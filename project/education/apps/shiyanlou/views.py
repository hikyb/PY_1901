from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator, Page
import time
from django.contrib.auth import login, logout, authenticate
import random, io
from PIL import Image, ImageDraw, ImageFont
from django.core.cache import cache


# Create your views here.


class RegistView(View):
    """注册"""
    def post(self, request):
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        verifycode = request.POST.get('captcha_v').lower()
        if not verifycode == cache.get('verify').lower():
            return HttpResponse("验证码错误")

        user = ShiyanlouUser.objects.create_user(username=nickname, email=email, password=password)

        return redirect(reverse("shiyanlou:index"))


def verify(request):
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 25
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 将验证码存储
    cache.set('verify', rand_str)
    # 构造字体对象
    font = ImageFont.truetype('LHANDW.TTF', 21)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 0), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 0), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 0), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 0), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')


class LoginView(View):
    """登录"""
    def post(self, request):
        nickname = request.POST.get('nickname')
        email = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=nickname, email=email, password=password)

        if user:
            login(request, user)
            return redirect(reverse('shiyanlou:index'))
        else:
            return HttpResponse("登录失败！")


class LogoutView(View):
    """退出登录"""
    def get(self, request):
        logout(request)
        return redirect(reverse('shiyanlou:index'))


class IndexView(View):
    """首页"""
    def get(self, request):
        # return HttpResponse("首页")
        pathcategory = PathCategory.objects.all()[:6]
        experimentcourse = ExperimentCourse.objects.all()[:4]
        return render(request, 'shiyanlou/index.html', locals())


class CourseView(View):
    """课程页"""
    def get(self, request, id):
        pathcategory = PathCategory.objects.all().order_by('title')[:5]
        category = Category.objects.all()
        categorycourse = Category.objects.get(pk=id).experimentcourse_set.all()[:9]

        tags = Tags.objects.all()
        experimentcourse = ExperimentCourse.objects.all()
        pagenum = request.GET.get("page")
        pagenum = 1 if not pagenum else pagenum

        if id == '1':
            page = Paginator(experimentcourse, 9).get_page(pagenum)
        else:
            page = Paginator(categorycourse, 9).get_page(pagenum)
        return render(request, 'shiyanlou/courses/index.html', {"page": page, "pathcategory": pathcategory, 'category': category})


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
        hotpath = PathCategory.objects.all().order_by('img')[:5]
        return render(request, 'shiyanlou/questions/index.html', {'hotpath': hotpath})


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
        hotpath = PathCategory.objects.all().order_by('desc')[:5]
        return render(request, 'shiyanlou/paths/show.html', locals())


class CourseShowView(View):
    """课程详情页"""
    def get(self, request, id):
        experimentcourse = ExperimentCourse.objects.get(pk=id)
        experimentcourse.view += 1
        experimentcourse.save()
        experimentlist = ExperimentCourse.objects.get(pk=id).experimentlist_set.all()
        return render(request, 'shiyanlou/courses/show.html', locals())


class PrivacyView(View):
    """关于我们"""
    def get(self, request):
        return render(request, 'shiyanlou/privacy/index.html')
