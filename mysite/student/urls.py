from django.conf.urls import url
from . import views
import django.contrib.auth.urls
from django.conf.urls import include
from django.contrib.auth import login

urlpatterns = [
    url('^$',views.home,name='home'),
    url('accounts/',include(django.contrib.auth.urls)),
    url('profile/$',views.profile,name = 'profile'),
    url('accounts/$',views.profile,name='profile'),
    url(r'logout/$', views.logout_i, name='logout'),
    url(r'courses/$',views.courses,name='courses'),
    url(r'marks/$',views.studmarks,name='marks'),
    url(r'studentmark/$',views.updatemarks,name='updatemarks'),
    url(r'chpassword/$', views.change_password, name='change_password'),


]