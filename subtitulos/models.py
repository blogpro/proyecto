from django.db import models

class SubtituloPost(models.Model):
	title = models.CharField(max_length=255)
	def __unicode__(self):
		return self.title 