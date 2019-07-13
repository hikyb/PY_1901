from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from comment.models import Comment
from blog.models import Article

# Create your views here.


class AddComment(View):
    def post(self, request, id):
        name = request.POST.get('name')
        email = request.POST.get('email')
        url = request.POST.get('url')
        content = request.POST.get('content')
        c = Comment()
        c.name = name
        c.email = email
        c.url = url
        c.content = content
        c.article = Article.objects.get(pk=id)
        c.save()
        return JsonResponse({"name": name, "content": content, "create_time": c.create_time})
