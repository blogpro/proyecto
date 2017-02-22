from django.db.models.base import Model
from django.forms import widgets
from rest_framework import serializers

from django.contrib.auth.models import User

from post.models import Post, Status_Post
from categorias.models import Categoria
from etiquetas.models import Etiqueta
from comentarios.models import Comentario
from imagenes.models import ImagenPost

from Angular2.models import Alumnos

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> USERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('first_name','last_name')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> STATUS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status_Post
		fields = ('title','descripcion','pk')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ETIQUETAS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class CategoriasSerializer(serializers.ModelSerializer):
	pk = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required=False, allow_blank=True, max_length=255)
	order = serializers.IntegerField(default=1,max_value=None, min_value=None)

	def create(self, validated_data):
		return Categoria.objects.create(**validated_data)

	class Meta:
		model = Categoria
		fields = ('pk','title','order',)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> POST <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class PostQuerySerializer(serializers.ModelSerializer):
	user = UserSerializer()
	status = StatusSerializer()
	class Meta:
		model = Post
		fields = ('id','title','status','user')
class EtiquetasSerializer(serializers.ModelSerializer):
	pk = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required=False, allow_blank=True, max_length=255)
	order = serializers.IntegerField(default=1,max_value=None, min_value=None)

	def create(self, validated_data):
		return Etiqueta.objects.create(**validated_data)

	class Meta:
		model = Etiqueta
		fields = ('pk','title','order',)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> USERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class ComentariosSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	post = PostQuerySerializer()
	class Meta:
		model = Comentario
		fields = ('id','user','post','descripcion','activo','fechahora',)
class ImagenSerializer(serializers.ModelSerializer):
	class Meta:
		model = ImagenPost
		fields = ('image',)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PROYECTO ANGULAR2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<		
class AlumnosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alumnos
		fields = ('pk','name','last_name','first_name','email',)						