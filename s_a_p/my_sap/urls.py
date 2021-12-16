from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("entries.urls")),
]

urlpatterns[
    path(
        "",
        views.profile,
        name="profile",
    ),
]

urlpatterns[
    path("", views.resource, name="resource"),
]

urlpatterns[
    path("", views.home, name="home"),
]
