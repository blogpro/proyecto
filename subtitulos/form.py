# -*- encoding: utf-8 -*-
from django.contrib.auth.models import *
from django import forms
from django.forms import widgets,DecimalField,DateTimeInput,TextInput,CheckboxInput,Select,PasswordInput,DateTimeInput,DateInput,HiddenInput,NullBooleanSelect,RadioSelect,CheckboxInput,Textarea,ImageField,SelectMultiple

from .models import SubtituloPost

class SubtituloForm(forms.ModelForm):
    class Meta:
        model = SubtituloPost
        fields = ('title',)
        widgets = {
            'title': TextInput(attrs={'class':'span12','id':'title', 'placeholder': 'Ingrese Subtitulo'}),
        }