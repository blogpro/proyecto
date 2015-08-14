# -*- encoding: utf-8 -*-
from django.contrib.auth.models import *
from django import forms
from django.forms import widgets,DecimalField,DateTimeInput,TextInput,CheckboxInput,Select,PasswordInput,DateTimeInput,DateInput,HiddenInput,NullBooleanSelect,RadioSelect,CheckboxInput,Textarea,ImageField,SelectMultiple

from .models import CodigosPost

class CodigosForm(forms.ModelForm):
    class Meta:
        model = CodigosPost
        fields = ('descripcion',)
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 5,'class':'span12'}),
        }    