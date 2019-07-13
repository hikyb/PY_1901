from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from .forms import ArticleForm, CommentForm
from django.core.paginator import Paginator, Page
from django.views.decorators.cache import cache_page

# Create your views here.


def getpage(request, object_list, per_page):
    pagenum = request.GET.get('page')
    pagenum = 1 if not pagenum else pagenum
    page = Paginator(object_list, per_page).get_page(pagenum)
    return page


class IndexView(View):
    """首页"""
    # @cache_page(60)
    def get(self, request):
        ads = Ads.objects.all()
        articles = Article.objects.all()
        page = getpage(request, articles, 2)
        return render(request, 'blog/index.html', {'page': page, 'ads': ads})


class SingleView(View):
    """详情页"""
    def get(self, request, id):
        article = get_object_or_404(Article, pk=id)
        article.views += 1
        article.save()
        cf = CommentForm()
        return render(request, 'blog/single.html', {'article': article, 'cf': cf})

    def post(self, request, id):
        article = get_object_or_404(Article, pk=id)
        cf = CommentForm(request.POST)
        comment = cf.save(commit=False)
        comment.article = article
        comment.save()
        return redirect(reverse('blog:single', args=(article.id,)))


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


class ArchivesView(View):
    def get(self, request, year, month):
        articles = Article.objects.filter(create_time__year=year, create_time__month=month)
        page = getpage(request, articles, 1)
        return render(request, 'blog/index.html', {'page': page})
