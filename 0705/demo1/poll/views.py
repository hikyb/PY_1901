from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Question, Choice, PollUser
from django.contrib.auth import login as lgi, logout as lgo, authenticate
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
    username = request.session.get('username')
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
        try:
            user = PollUser.objects.create_user(username=username, password=password)
        except:
            return None
        if user:
            return redirect(reverse('poll:login'))
        else:
            return redirect(reverse('poll:regist'))


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
        user = authenticate(request, username=username, password=password)
        if user:
            lgi(request, user)
            return redirect(reverse('poll:index'))
        else:
            return redirect(reverse('poll:login'))


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

