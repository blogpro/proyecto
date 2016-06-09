# -*- encoding: utf-8 -*-
from django.db import models

class ImagenPost(models.Model):
	image = models.ImageField(upload_to='images/post', verbose_name='Imágen', blank=True, null=True)
	def __unicode__(self):
		return self.image.url 