# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.forms import widgets,DecimalField,DateTimeInput,TextInput,CheckboxInput,Select,PasswordInput,DateTimeInput,DateInput,HiddenInput,NullBooleanSelect,RadioSelect,CheckboxInput,Textarea,SelectMultiple


from .models import Comentario

class ComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = ('descripcion',)
		widgets = {
			'descripcion': Textarea(attrs={'class':'form-control','id':'web','rows':6, 'cols':80,'required':'required'}),
	}          
