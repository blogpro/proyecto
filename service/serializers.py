from django.db.models.base import Model
from django.forms import widgets
from rest_framework import serializers

from django.contrib.auth.models import User

from post.models import Post, Status_Post
from categorias.models import Categoria

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('first_name',)

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status_Post
		fields = ('title',)		

class CategoriasSerializer(serializers.ModelSerializer):
	pk = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required=False, allow_blank=True, max_length=100)

	def create(self, validated_data):
		return	Categoria.objects.create(title=validated_data['title'])

	class Meta:
		model = Categoria
		fields = ('pk','title',)

class PostQuerySerializer(serializers.ModelSerializer):
	user = UserSerializer()
	status = StatusSerializer()
	class Meta:
		model = Post
		fields = ('id','title','status','user')