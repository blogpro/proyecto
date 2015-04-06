# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.forms import widgets,DecimalField,DateTimeInput,TextInput,CheckboxInput,Select,PasswordInput,DateTimeInput,DateInput,HiddenInput,NullBooleanSelect,RadioSelect,CheckboxInput,Textarea,SelectMultiple

import datetime 
import calendar
import time
from django.utils.timezone import utc

from datetime import date, timedelta


from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','etiquetas','categoria',)
        widgets = {
            'title': TextInput(attrs={'class':'span12','id':'Descripcion','placeholder':'Descripcion'}),
            'etiquetas': SelectMultiple(attrs={'class':'span12','size':'10'}),
            'categoria': Select(attrs={'class':'span12','id':'categoria'}),
        }          
