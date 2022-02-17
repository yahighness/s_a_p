from django.shortcuts import render
from django.urls import path, re_path
from django.views.generic.base import RedirectView
from . import views

urlpatterns=[
    path("", RedirectView.as_view(url="/home/")),
    path("home/", views.home, name="home"),
    path("blog/",views.blog,name="blog"),
    path("resource/", views.resource, name="resource"),
    path("client/", views.client, name="client"),
    re_path(r"^edit/(?P<post_id>\d+)$", views.edit_post, name="edit-post"),
    re_path(r"^remove_tag/(?P<post_id>\d+)/(?P<tag_id>\d+)$", views.remove_tag, name="remove-tag"),
    re_path(r"^delete/(?P<post_id>\d+)$", views.delete_post, name="delete-post"),
]
