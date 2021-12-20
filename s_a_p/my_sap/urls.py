from django.contrib import admin
from django.urls import path, include, resource, home, client



from . import views



urlpatterns = [
    path(“admin/“, admin.site.urls), 
    path(“”, include(“my_sap.urls”)),
]
urlpatterns[
    path(
        “”,
        views.profile,
        name=“profile”,
    ),
]
urlpatterns[
    path(“”, views.resource, name=“resource”),
]
urlpatterns[
    path(“”, views.home, name=“home”),
]
urlpatterns = [
    path(“”, views.EntryListView.as_view(), name=“entry-list”),
    path(“entry/<int:pk>“, views.EntryDetailView.as_view(), name=“entry-detail”),
    path(“create”, views.EntryCreateView.as_view(), name=“entry-create”),
    path(
        “entry/<int:pk>/update”,
        views.EntryUpdateView.as_view(),
        name=“entry-update”,
    ),
    path(
        “entry/<int:pk>/delete”,
        views.EntryDeleteView.as_view(),
        name=“entry-delete”,
    ),
]