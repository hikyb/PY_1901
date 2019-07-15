from django.shortcuts import render, redirect, reverse

# Create your views here.

from django.http import HttpResponse
from .models import Question, Choice


def index(request):
    # return HttpResponse("首页")
    questions = Question.objects.all()
    return render(request, 'vote/index.html', {'questions': questions})


def choice(request, id):
    # return HttpResponse("成功")
    question = Question.objects.get(pk=id)
    if request.method == 'GET':
        return render(request, 'vote/choice.html', {'question': question})
    elif request.method == 'POST':
        choiceid = request.POST.get('choice')
        choice = Choice.objects.get(pk=choiceid)
        choice.poll += 1
        choice.save()
        # 没有重定向，刷新浏览器会再次发起post请求，结果不对
        # return render(request, 'vote/detail.html', {'question': question})
        return redirect(reverse('vote:detail', args=(id, )))


def detail(request, id):
    # return HttpResponse("详情页")
    question = Question.objects.get(pk=id)
    return render(request, 'vote/detail.html', {'question': question})
