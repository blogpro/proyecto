from django.db.models.base import Model
from django.forms import widgets
from rest_framework import serializers

from django.contrib.auth.models import User

from post.models import Post, Status_Post

class UserPerSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('first_name',)

class PostQuerySerializer(serializers.ModelSerializer):
	user = UserPerSerializer()
	class Meta:
		model = Post
		fields = ('id','title','status','user')