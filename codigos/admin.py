from django.contrib import admin
from django import forms

from .models import CodigosPost


 
# class MyModelForm(forms.ModelForm ):
#     descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows': 15,'cols': 80,}))
 
#     class Meta:
#         model = CodigosPost
 
# class MyModelAdmin(admin.ModelAdmin):
#     form = MyModelForm


# # Register your models here.
# admin.site.register(CodigosPost,MyModelAdmin)

admin.site.register(CodigosPost)