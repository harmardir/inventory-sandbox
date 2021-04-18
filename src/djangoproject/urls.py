from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from djangoapp.views import home , computer_entry , computer_list , computer_edit , computer_delete

urlpatterns = [
    url('admin/',admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^computer_entry/$',computer_entry, name='computer_entry'),
    url(r'^computer_list/$', computer_list, name='computer_list'),
    url(r'^computer_list/(?P<id>\d+)/$', computer_edit, name='computer_edit'),
    url(r'^computer_list/(?P<id>\d+)/delete$',computer_delete, name='computer_delete'),
]
