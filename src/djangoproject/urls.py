from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from djangoapp.views import home

urlpatterns = [
    url('admin/',admin.site.urls),
    url(r'^$', home, name='home'),
]
