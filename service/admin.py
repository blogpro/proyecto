from django.contrib import admin

from .models import UserService, Note

# Register your models here.
admin.site.register(UserService)
admin.site.register(Note)

