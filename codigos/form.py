# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.forms import widgets,DecimalField,DateTimeInput,TextInput,CheckboxInput,Select,PasswordInput,DateTimeInput,DateInput,HiddenInput,NullBooleanSelect,RadioSelect,CheckboxInput,Textarea,SelectMultiple

import datetime 
import calendar
import time
from django.utils.timezone import utc

from datetime import date, timedelta


from .models import CodigosPost

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = CodigosPost
#         fields = ('descripcion',)
#         widgets = {
#             'descripcion': Textarea(attrs={'class':'span12','id':'Descripcion','placeholder':'Descripcion'}),
#         }          
