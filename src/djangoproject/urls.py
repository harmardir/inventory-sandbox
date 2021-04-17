from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from djangoapp.views import home , computer_entry , computer_list

urlpatterns = [
    url('admin/',admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^computer_entry/$',computer_entry, name='computer_entry'),
    url(r'^computer_list/$', computer_list, name='computer_list'),
]
