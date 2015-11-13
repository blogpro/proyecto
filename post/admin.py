from django.contrib import admin

from .models import Status_Post, Post,PostAdd

# Register your models here.
admin.site.register(Status_Post)
admin.site.register(Post)
admin.site.register(PostAdd)

