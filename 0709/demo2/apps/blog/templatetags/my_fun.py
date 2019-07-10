"""
自定义模板表达式
扩展Django原有功能
"""

from django.template import library
from blog.models import Article

register = library.Library()


@register.simple_tag
def getlastestarticles(num=3):
    return Article.objects.order_by('-create_time')[:num]
