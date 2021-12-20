from django.contrib import admin
from .models import Home, Client, Resource, Blog

# Register your models here.
admin.site.register(Home)
admin.site.register(Client)
admin.site.register(Resource)
admin.site.register(Blog)
