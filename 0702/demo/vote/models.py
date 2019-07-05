from django.db import models

# Create your models here.


class Question(models.Model):
    """问题"""
    content = models.CharField(max_length=50)

    def __str__(self):
        return self.content

    # def textcontent(self):
    #     return self.content
    # textcontent.short_description = "问题描述"


class Choice(models.Model):
    """选项"""
    content = models.CharField(max_length=50)
    poll = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
