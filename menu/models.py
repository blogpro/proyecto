from django.db import models

# Create your models here.
from django.template import defaultfilters
class Menu(models.Model):
	descripcion = models.CharField(max_length=255)
	slug = models.SlugField()
	order = models.PositiveIntegerField()

	def __unicode__(self):
		return self.descripcion
		
	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.descripcion)
		super(Menu, self).save(*args, **kwargs)	

