from django.urls import path
from . import views
urlpatterns=[
    path("home/", views.home, name="home"),
    path("blog/",views.blog,name="blog"),
    path("resource/", views.resource, name="resource"),
    path("client/", views.client, name="client")
]