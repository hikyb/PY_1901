from django.db import models

# Create your models here.


class ChoiceManager(models.Manager):
    """自定义管理器"""
    def increase(self, id):
        c = self.get(pk=id)
        c.vote += 1
        c.save()


class Question(models.Model):
    """问题"""
    desc = models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.desc

    class Meta:
        # verbose_name = "问题表"
        verbose_name_plural = "问题表"
        # db_table = "问题表"   # 数据库显示
        ordering = ['-pub_date']  # 排序，增加开销


class Choice(models.Model):
    """选项"""
    desc = models.CharField(verbose_name='选项', help_text='选项描述', max_length=20)
    # verbose_name在admin后台可以看到所设置的名称字样，help_text对该内容的描述，null=True, blank=True
    vote = models.IntegerField(verbose_name='票数', help_text='选项票数', default=0, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    myobjects = ChoiceManager()

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name_plural = "选项表"
        # ordering = ['-vote']



