from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("client/", views.client, name="client"),
    path("resource/", views.resource, name="resource"),
    path("blog/", views.blog, name="blog"),
]