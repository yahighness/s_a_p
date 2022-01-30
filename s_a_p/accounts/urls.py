from django.urls import path
from django.views.generic.base import RedirectView
from . import views
urlpatterns=[
    path("", RedirectView.as_view(pattern_name="login")),
    path("login/", views.login, name="login"),
  #  path("logout/",views.logout,name="logout"),
  #  path("create/", views.create_account, name="create_account"),
]
