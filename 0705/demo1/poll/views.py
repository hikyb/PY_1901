from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Question, Choice
# Create your views here.


def index(request):
    """首页"""
    # return HttpResponse('首页')
    questions = Question.objects.all()
    return render(request, 'poll/index.html', locals())


def detail(request, id):
    """选择详情页"""
    question = Question.objects.get(pk=id)
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
    # return HttpResponse('结果显示页')
    question = Question.objects.get(pk=id)
    return render(request, 'poll/result.html', {'question': question})


