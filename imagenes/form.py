# -*- encoding: utf-8 -*-
from django.contrib.auth.models import *
from django import forms
from django.forms import widgets,DecimalField,DateTimeInput,TextInput,CheckboxInput,Select,PasswordInput,DateTimeInput,DateInput,HiddenInput,NullBooleanSelect,RadioSelect,CheckboxInput,Textarea,ImageField,SelectMultiple

from .models import ImagenPost

class ImegenForm(forms.ModelForm):
    class Meta:
        model = ImagenPost
        fields = "__all__" 