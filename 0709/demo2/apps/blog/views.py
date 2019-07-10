from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from .forms import ArticleForm
from django.core.paginator import Paginator, Page

# Create your views here.


class IndexView(View):
    """首页"""
    def get(self, request):
        ads = Ads.objects.all()
        articles = Article.objects.all()
        pagenum = request.GET.get('page')
        pagenum = 1 if not pagenum else pagenum
        page = Paginator(articles, 2).get_page(pagenum)
        return render(request, 'blog/index.html', {'page': page, 'ads': ads})


class SingleView(View):
    """详情页"""
    def get(self, request, id):
        article = Article.objects.all()
        return render(request, 'blog/single.html')

    def post(self, request, id):
        return render(request, 'blog/single.html')


class AddArticle(View):
    """添加文章"""
    def get(self, request):
        af = ArticleForm()
        return render(request, 'blog/addarticle.html', locals())

    def post(self, requst):
        af = ArticleForm(requst.POST)
        print(af.is_valid())
        if af.is_valid():
            article = af.save(commit=False)
            article.category = Catrgory.objects.first()
            article.author = User.objects.first()
            article.tags = Article.objects.first().tags
            article.save()
            return redirect(reverse('blog:index'))
        else:
            return HttpResponse('文章发表失败')

