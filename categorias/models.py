from django.db import models

# Create your models here.
class Categoria(models.Model):
	title = models.CharField(max_length=255)
	order = models.PositiveIntegerField()

	def __unicode__(self):
		return self.title 
