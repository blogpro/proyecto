from django.db import models
from django.contrib.auth.models import User


class UserService(models.Model):
	email = models.CharField(max_length=255)
	def __unicode__(self):
		return self.email 


class Note(models.Model):
	user = models.ForeignKey(UserService,blank=True, null=True)
	title = models.CharField(max_length=255)
	text = models.CharField(max_length=2000)
	fecha_registro = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.title
