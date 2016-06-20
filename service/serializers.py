from django.db.models.base import Model
from django.forms import widgets
from rest_framework import serializers

from post.models import Post

class PostQuerySerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('id','title','status','user')