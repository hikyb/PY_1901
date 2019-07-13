from django import forms
from .models import Article
from comment.models import Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'col-md-6'})
        },
        labels = {
            'title': '文章标题',
            'body': '文章内容'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'url', 'email', 'content']
