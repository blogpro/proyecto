from django.db import models

# Create your models here.
class Alumnos(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30, blank=True)

	def __unicode__(self):
		return self.name 

class Productos(models.Model):
	name = models.CharField(max_length=255)
	descripcion = models.CharField(max_length=500)
	precio = models.FloatField(null=True, blank=True, default=0.0)
	stock = models.IntegerField(default=0)
	imgbase64 = models.TextField()
	def __unicode__(self):
		return self.name 