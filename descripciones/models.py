from django.db import models
from ckeditor.fields import RichTextField

class DescripcionPost(models.Model):
	#descripcion = models.CharField(max_length=255)
	descripcion=RichTextField()  # Usamos  RichTextField()
	def __unicode__(self):
		return self.descripcion 