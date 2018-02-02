from django.conf.urls import include
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.contrib.auth import urls
from django.contrib.auth import views


import django

urlpatterns = [
    url('admin/', admin.site.urls),
    url('',include('student.urls')),

]


