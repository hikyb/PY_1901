from django.shortcuts import render

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
    return render(request, 'vote/choice.html', {'question': question})
