from django.contrib import admin
from .models import Profile, Tag, Post, Resource

# Register your models here.
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Resource)
