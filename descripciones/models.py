from django.db import models
from ckeditor.fields import RichTextField

class DescripcionPost(models.Model):
	descripcion=RichTextField()  # Usamos  RichTextField()
	def __unicode__(self):
		return self.descripcion 