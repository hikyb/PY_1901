from django.shortcuts import render, redirect, reverse

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import BookInfo, HeroInfo



def index(request):
    """首页"""
    # return HttpResponse("首页 <a href='/list/'>跳转到列表页</a>")

    # cont = {"username": "kyb"}
    # # 获取模板
    # temp1 = loader.get_template("booktest/index.html")
    # # 使用模板渲染字典参数
    # result = temp1.render(cont)
    # # 将渲染的模板返回
    # return HttpResponse(result)

    cont = {"username": "kyb"}
    return render(request, 'booktest/index.html', cont)


def list(request):
    """列表页"""
    # s = """
    # <br>
    # <a href='/detail/1'>跳转到详情页1</a>
    # <br>
    # <a href='/detail/2'>跳转到详情页2</a>
    # <br>
    # <a href='/detail/3'>跳转到详情页3</a>
    # """
    # return HttpResponse("列表页 %s" % (s,))

    # books = BookInfo.objects.all()
    # tem2 = loader.get_template("booktest/list.html")
    # result = tem2.render({"books": books})
    # return HttpResponse(result)

    books = BookInfo.objects.all()
    return render(request, 'booktest/list.html', {'books': books})


def detail(request, id):
    """详情页"""
    # return HttpResponse("详情页%s <a href='/index/'>跳转到首页</a>" % (id,))

    # book = BookInfo.objects.get(pk=id)
    # temp3 = loader.get_template("booktest/detail.html")
    # result = temp3.render({"book": book})
    # return HttpResponse(result)

    book = BookInfo.objects.get(pk=id)
    return render(request, 'booktest/detail.html', {'book': book})


def deletebook(request, id):
    """删除书籍"""
    # return HttpResponse('删除成功')
    book = BookInfo.objects.get(pk=id)
    book.delete()
    return redirect(reverse('booktest:list'))


def addhero(request, id):
    # return HttpResponse("添加成功")
    book = BookInfo.objects.get(pk=id)
    if request.method == 'GET':
        return render(request, 'booktest/addhero.html', {'book': book})
    elif request.method == 'POST':
        name = request.POST.get('heroname')
        gender = request.POST.get('gender')
        content = request.POST.get('content')
        hero = HeroInfo(name=name, gender=gender, content=content, book=book)
        hero.save()
        return redirect(reverse('booktest:detail', args=(id,)))


def deletehero(request, id):
    """删除英雄"""
    hero = HeroInfo.objects.get(pk=id)
    bookid = hero.book.id
    hero.delete()
    # return HttpResponse("删除成功")
    # return HttpResponseRedirect('/detail/'+str(bookid)+'/')
    # result = reverse('booktest:detail', args=(bookid,))
    # return redirect('/detail'+str(bookid)+'/')

    return redirect(reverse('booktest:detail', args=(bookid,)))
