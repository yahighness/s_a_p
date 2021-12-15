from django.urls import path
from . import views

urlpatterns[
    path(
        "",
        views.blog,
        name="blog",
    ),
]

urlpatterns[
    path("", views.resources, name="resources"),
]

urlpatterns[
    path("", views.home, name="home"),
]
