from django.conf.urls import url
from . import views

app_name = 'vote'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^choice/(\d+)/$', views.choice, name='choice'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
]
