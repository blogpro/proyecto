# -*- encoding: utf-8 -*-
from django.contrib.auth.models import *
from django import forms

from .models import DescripcionPost

from suit_ckeditor.widgets import CKEditorWidget

class DescripcionForm(forms.ModelForm):
    descripcion = forms.CharField(widget=CKEditorWidget())#tiene que ser el mismo nombre del campo en la base de datos
    class Meta:
        model = DescripcionPost 
        exclude = ()   