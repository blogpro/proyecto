# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.forms import widgets,DecimalField,DateTimeInput,TextInput,CheckboxInput,Select,PasswordInput,DateTimeInput,DateInput,HiddenInput,NullBooleanSelect,RadioSelect,CheckboxInput,Textarea,SelectMultiple,FileInput

import datetime 
import calendar
import time
from django.utils.timezone import utc

from datetime import date, timedelta

from suit_ckeditor.widgets import CKEditorWidget
from .models import Post

class PostForm(forms.ModelForm):
	descripcion = forms.CharField(widget=CKEditorWidget())#tiene que ser el mismo nombre del campo en la base de datos
	class Meta:
		model = Post
		fields = ('status','title','etiquetas','categoria','descripcion','image')
		widgets = {
			'status': Select(attrs={'class':'form-control','id':'status'}),
			'title': TextInput(attrs={'class':'form-control','id':'Descripcion','placeholder':'Descripcion'}),
			'etiquetas': SelectMultiple(attrs={'class':'form-control','size':'5'}),
			'categoria': Select(attrs={'class':'form-control','id':'categoria'}),
	}          
