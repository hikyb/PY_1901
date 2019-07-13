from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice, PollUser
from django.contrib.auth import login as lgi, logout as lgo, authenticate
from PIL import Image, ImageDraw, ImageFont
import random, io
from django.core.cache import cache
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer

# Create your views here.


def checklogin(fun):
    """检查是否登录的装饰函数"""
    def check(request, *args):
        # username = request.COOKIES.get('username')
        # username = request.session.get('username')
        if request.user and request.user.is_authenticated:
        # if username:
            return fun(request, *args)
        else:
            return redirect(reverse('poll:login'))
    return check


def index(request):
    """首页"""
    # cookie方法
    # return HttpResponse('首页')
    # username = request.COOKIES.get('username')

    # session方法
    # username = request.session.get('username')
    # questions = Question.objects.all()
    # return render(request, 'poll/index.html', locals())

    # Django自带授权
    # print(request.user, request.user.is_authenticated)  # 没有用户登录，request.user默认为匿名用户
    # username = request.user
    questions = Question.objects.all()
    return render(request, 'poll/index.html', locals())


@checklogin
def detail(request, id):
    """选择详情页"""
    try:
        username = request.session.get('username')
        question = Question.objects.get(pk=id)
    except Question.DoesNotExist:  # Question.objects.get(pk=20)
        return HttpResponse('id非法')
    except Question.MultipleObjectsReturned:  # Question.objects.get(pk__gt=1)
        return HttpResponse('id非法')
    if request.method == 'GET':
        return render(request, 'poll/detail.html', locals())
    elif request.method == 'POST':
        choiceid = request.POST.get('choice')
        # choice = Choice.objects.get(pk=choiceid)
        # choice.vote += 1
        # choice.save()
        Choice.myobjects.increase(choiceid)

        return redirect(reverse('poll:result', args=(id,)))


def result(request, id):
    """结果显示页"""
    username = request.session.get('username')
    # return HttpResponse('结果显示页')
    question = Question.objects.get(pk=id)
    return render(request, 'poll/result.html', {'question': question, 'username': username})


def regist(request):
    """注册"""
    if request.method == 'GET':
        return render(request, 'poll/regist.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        recvlist = [request.POST.get('email')]
        try:
            user = PollUser.objects.create_user(username=username, password=password)
            newuser = PollUser.objects.last()
            # 定义序列化工具
            serializer = TimedJSONWebSignatureSerializer(settings.SECRET_KEY)
            serializerstr = serializer.dumps({'newuserid': newuser.id}).decode('utf-8')  # dumps将对象序列化成字符串  loads将字符串反序列化成对象

            mail = EmailMultiAlternatives("Python发送HTML邮件", "<h1><a href='http://192.168.0.0.1:8000/active/%s/'>"
                                                            "点我激活</a></h1>" %(serializerstr), settings.EMAIL_HOST_USER, recvlist)
            mail.content_subtype = 'html'
            mail.send()
            newuser.is_active = False
            newuser.save()
        except:
            return None
        if user:
            return redirect(reverse('poll:login'))
        else:
            return redirect(reverse('poll:regist'))


def active(request, id):
    """激活用户邮箱"""
    # 定义序列化工具
    serializer = TimedJSONWebSignatureSerializer(settings.SECRET_KEY)
    serializerobj = serializer.loads(id)  # dumps将对象序列化成字符串  loads将字符串反序列化成对象
    uid = serializerobj['newuserid']

    get_object_or_404(PollUser, pk=uid).is_active = True
    return HttpResponse("恭喜，账号激活成功！")


def login(request):
    """登录"""
    if request.method == 'GET':
        return render(request, 'poll/login.html')
    elif request.method == 'POST':
        # 1.使用cookie存储信息
        # response = redirect(reverse('poll:index'))
        # response.set_cookie('username', request.POST.get('username'))
        # return response

        # 2.使用session存储信息
        # request.session['username'] = request.POST.get('username')
        # return redirect(reverse('poll:index'))

        username = request.POST.get('username')
        password = request.POST.get('password')
        verifycode = request.POST.get('verify')
        if not verifycode == cache.get('verify').lower():
            return HttpResponse('验证码错误')
        user = authenticate(request, username=username, password=password)
        if user:
            lgi(request, user)
            return redirect(reverse('poll:index'))
        else:
            return redirect(reverse('poll:login'))


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
    draw.text((5, 1), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 1), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 1), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 1), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')


def logout(request):
    """退出"""
    # res = redirect(reverse('poll:index'))
    # res.delete_cookie('username')
    # return res

    # request.session.flush()
    # return redirect(reverse('poll:index'))

    lgo(request)
    return redirect(reverse('poll:index'))


"""
from django.contrib.auth import login, logout, authenticated
is_authenticated
request.user
request.user.is_authenticated
objects.create_user
user.set_password
user.check_password
login(request, user)
logout(request)
"""

