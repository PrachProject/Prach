from django.conf.urls import url
from django.contrib import admin

from posts import views
urlpatterns = [
	url(r'^$', "posts.views.post_list"),
    url(r'^create/$', "posts.views.post_create"),
    url(r'^detail/$', "posts.views.post_detail"),
    url(r'^update/$', "posts.views.post_update"),
    url(r'^delete/$', "posts.views.post_delete"),
     #url(r'^posts/', "<appname>.view.<function_name"),
]
