from django.db import models

# Create your models here.
class Alumnos(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30, blank=True)

	def __unicode__(self):
		return self.name 
