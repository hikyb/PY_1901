from django.db import models
from blog.models import Article

# Create your models here.


class Comment(models.Model):
    """文章评论"""
    name = models.CharField(max_length=20)
    url = models.URLField(blank=True, null=True, default='http://www.baidu.com')
    email = models.EmailField(blank=True, null=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
