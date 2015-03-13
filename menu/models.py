from django.db import models

# Create your models here.

class Menu(models.Model):
	descripcion = models.CharField(max_length=255)
	order = models.PositiveIntegerField()

	def __unicode__(self):
		return self.descripcion 
