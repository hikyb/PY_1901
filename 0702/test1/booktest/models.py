from django.db import models

# Create your models here.


class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class HeroInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    content = models.CharField(max_length=100)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
