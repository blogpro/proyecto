from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


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

# This code is triggered whenever a new user has been created and saved to the database

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)