from django.db import models
from django import forms
from django.contrib.auth.models import User

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


class PollUser(User):
    """用户类"""
    user = models.CharField(max_length=20)


# class LoginForm(forms.Form):
#     """登录表单类"""
#     username = forms.CharField(label='用户名', max_length=20, required=True, widget=forms.TextInput(
#         attrs={'id': 'username', 'class': 'form-control', 'placehold': '输入用户名'}
#     )),
#     password = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(
#         attrs={'class': 'form-control', 'id': 'password', 'placehold': '输入密码'}
#     ))


# class RegistForm(forms.ModelForm):
#     """注册表单类"""
#     repeatpassword = forms.CharField(label='重复密码', required=True, widget=forms.PasswordInput(
#         attrs={'class': 'form-control', 'id': 'registpassword2', 'placehold': '输入确认密码'}
#     ))
#     class Meta:
#         models = PollsUser
#         fields = ['username', 'password', 'telephone']
#         widgets = {'username': forms.TextInput(attrs={'id': 'registusername', 'placehold': ''})}

