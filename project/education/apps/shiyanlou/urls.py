from django.conf.urls import url
from . import views

app_name = 'shiyanlou'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^course/$', views.CourseView.as_view(), name='course'),
    url(r'^developer/$', views.DeveloperView.as_view(), name='developer'),
    url(r'^paths/$', views.PathsView.as_view(), name='paths'),
    url(r'^discussion/$', views.DiscussionView.as_view(), name='discussion'),
    url(r'^discussion/detail/$', views.DiscussionDetailView.as_view(), name='discussion_detail'),
    url(r'^bootcamp/$', views.BootcampView.as_view(), name='bootcamp'),
    url(r'^bootcamp/detail/(\d+)/$', views.BootcampDeatilView.as_view(), name='bootcamp_detail'),
    url(r'^vip/$', views.VipView.as_view(), name='vip'),
    url(r'^paths/show/(\d+)/$', views.PathShowView.as_view(), name='show'),
    url(r'^course/show/(\d+)/$', views.CourseShowView.as_view(), name='course_show'),
    url(r'^privacy/$', views.PrivacyView.as_view(), name='privacy'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^regist/$', views.RegistView.as_view(), name='regist'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]
