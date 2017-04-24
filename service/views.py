# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404,render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, FormView, DetailView, UpdateView

#Seguridad para las vistas
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator


from rest_framework import status,authentication
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated, AllowAny


from django.core.urlresolvers import reverse

from categorias.models import Categoria
from etiquetas.models import Etiqueta
from post.models import Post, Status_Post
from comentarios.models import Comentario
from imagenes.models import ImagenPost

from Angular2.models import Alumnos, Productos

from .serializers import PostQuerySerializer, CategoriasSerializer, EtiquetasSerializer, ComentariosSerializer, ImagenSerializer, StatusSerializer, AlumnosSerializer, ProductosSerializer
from post.ModelPost import ComentariosMixin

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> POST <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class ServicePostQuery(APIView):
	def get(self, request, *args, **kwargs):
		serializers = Post.objects.all().order_by('-id')
		try:
			serializer = PostQuerySerializer(serializers, many=True)
		except (TypeError, ValueError) as err:
			print 'ERROR:', err
		return Response(serializer.data)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> CATEGORIAS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class ServiceCategoriasQuery(APIView):
	def get(self, request, *args, **kwargs):
		if 'pk' in self.kwargs:
			ObjCategoria = Categoria.objects.get(pk=self.kwargs['pk'])
			data = {
				'pk':ObjCategoria.id,
				'title':ObjCategoria.title
			}
			return Response(data)
		serializers = Categoria.objects.all().order_by('-id')
		try:
			serializer = CategoriasSerializer(serializers, many=True)
		except (TypeError, ValueError) as err:
			print 'ERROR:', err
		return Response(serializer.data)
	def post(self, request, *args, **kwargs):
		title = request.data['title']
		ObjModel = Categoria()
		ObjModel.title = request.data['title']
		ObjModel.order = 0
		ObjModel.save()

		data = {
			'setCod': 0,
		}
		return Response(data)
	def put(self, request, *args, **kwargs):
		Categoria.objects.filter(pk=request.data['pk']).update(title=request.data['title'])
		data = {
			'setCod': 0,
		}
		return Response(data)
	def delete(self, request, *args, **kwargs):
		post = Categoria.objects.get(pk=self.kwargs['pk']).delete()
		data = {
			'setCod': 0,
		}
		return Response(data)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ETIQUETAS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class ServiceEtiquetasQuery(APIView):
	def get(self, request, *args, **kwargs):
		if 'pk' in self.kwargs:
			ObjModel = Etiqueta.objects.get(pk=self.kwargs['pk'])
			data = {
				'pk':ObjModel.id,
				'title':ObjModel.title
			}
			return Response(data)
		serializers = Etiqueta.objects.all().order_by('-id')
		try:
			serializer = EtiquetasSerializer(serializers, many=True)
		except (TypeError, ValueError) as err:
			print 'ERROR:', err
		return Response(serializer.data)
	def post(self, request, *args, **kwargs):
		title = request.data['title']
		ObjModel = Etiqueta()
		ObjModel.title = request.data['title']
		ObjModel.order = 0
		ObjModel.save()

		data = {
			'setCod': 0,
		}
		return Response(data)
	def put(self, request, *args, **kwargs):
		Etiqueta.objects.filter(pk=request.data['pk']).update(title=request.data['title'])
		data = {
			'setCod': 0,
		}
		return Response(data)
	def delete(self, request, *args, **kwargs):
		post = Etiqueta.objects.get(pk=self.kwargs['pk']).delete()
		data = {
			'setCod': 0,
		}
		return Response(data)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Comentarios <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class ServiceComentariosQuery(ComentariosMixin,APIView):
	def get(self, request, *args, **kwargs):
		if 'pk' in self.kwargs:
			return Response(self.comenGet(self.kwargs['pk']))
		serializers = Comentario.objects.filter(activo=False).order_by('-id')
		try:
			serializer = ComentariosSerializer(serializers, many=True)
		except (TypeError, ValueError) as err:
			print 'ERROR:', err
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
		ObjPost = Post.objects.get(pk=request.data['post'])
		ObjModel = Comentario()
		ObjModel.user = self.request.user
		ObjModel.descripcion = request.data['message']
		ObjModel.post = ObjPost
		ObjModel.save()

		data = {
			'setCod': 0,
		}
		return Response(data)
	def put(self, request, *args, **kwargs):
		Comentario.objects.filter(pk=request.data['pk']).update(activo=True)
		data = {
			'setCod': 0,
		}
		return Response(data)
	def delete(self, request, *args, **kwargs):
		post = Comentario.objects.get(pk=self.kwargs['pk']).delete()
		data = {
			'setCod': 0,
		}
		return Response(data)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Imagen <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class ServiceImagenQuery(APIView):
	def get(self, request, *args, **kwargs):
		serializers = ImagenPost.objects.all().order_by('-id')[:3]
		try:
			serializer = ImagenSerializer(serializers, many=True)
		except (TypeError, ValueError) as err:
			print 'ERROR:', err
		return Response(serializer.data)
	def post(self, request, *args, **kwargs):
		vFile = request.FILES['0']#Se declara como longitud para ecuperar ya que puede venir mas de 1.

		ObjModel = ImagenPost()
		ObjModel.image = vFile
		ObjModel.save()

		data = {
			'setCod': 0
		}
		return Response(data)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> STATUS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class ServiceStatusQuery(APIView):
	permission_classes = (AllowAny,)

	def get(self, request, *args, **kwargs):
		if 'pk' in self.kwargs:
			ObjModel = Status_Post.objects.get(pk=self.kwargs['pk'])
			data = {
				'pk':ObjModel.id,
				'title':ObjModel.title,
				'descripcion':ObjModel.descripcion
			}
			return Response(data)
		serializers = Status_Post.objects.all().order_by('-id')
		try:
			serializer = StatusSerializer(serializers, many=True)
		except (TypeError, ValueError) as err:
			print 'ERROR:', err
		return Response(serializer.data)
	def post(self, request, *args, **kwargs):
		ObjModel = Status_Post()
		ObjModel.title = request.data['title']
		ObjModel.descripcion = request.data['descripcion']
		ObjModel.save()

		data = {
			'setCod': 0,
		}
		return Response(data)
	def put(self, request, *args, **kwargs):
		Status_Post.objects.filter(pk=request.data['pk']).update(title=request.data['title'],descripcion=request.data['descripcion'])
		data = {
			'setCod': 0,
		}
		return Response(data)
	def delete(self, request, *args, **kwargs):
		post = Status_Post.objects.get(pk=self.kwargs['pk']).delete()
		data = {
			'setCod': 0,
		}
		return Response(data)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PROYECTO ANGULAR2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class AlumnosServiceQuery(APIView):
	# permission_classes = (AllowAny,)

	def get(self, request, *args, **kwargs):
		if 'pk' in self.kwargs:
			ObjModel = Alumnos.objects.get(pk=self.kwargs['pk'])
			data = {
				'pk':ObjModel.id,
				'name':ObjModel.name,
				'last_name':ObjModel.last_name,
				'first_name':ObjModel.first_name,
				'email':ObjModel.email
			}
			return Response(data)
		serializers = Alumnos.objects.all().order_by('-id')
		try:
			serializer = AlumnosSerializer(serializers, many=True)
		except (TypeError, ValueError) as err:
			print 'ERROR:', err
		return Response(serializer.data)
	def post(self, request, *args, **kwargs):
		ObjModel = Alumnos()
		ObjModel.name = request.data['name']
		ObjModel.last_name = request.data['last_name']
		ObjModel.first_name = request.data['first_name']
		ObjModel.email = request.data['email']
		ObjModel.save()

		data = {
			'setCod': 0,
		}
		return Response(data)
	def put(self, request, *args, **kwargs):
		Alumnos.objects.filter(pk=request.data['pk']).update(name=request.data['name'],first_name=request.data['first_name'],last_name=request.data['last_name'],email=request.data['email'])
		data = {
			'setCod': 0,
		}
		return Response(data)
	def delete(self, request, *args, **kwargs):
		post = Alumnos.objects.get(pk=self.kwargs['pk']).delete()
		data = {
			'setCod': 0,
		}
		return Response(data)

class ProductosviceQuery(APIView):
	permission_classes = (AllowAny,)

	def get(self, request, *args, **kwargs):
		if 'pk' in self.kwargs:
			ObjModel = Productos.objects.get(pk=self.kwargs['pk'])
			data = {
				'pk':ObjModel.id,
				'name':ObjModel.name,
				'last_name':ObjModel.last_name,
				'first_name':ObjModel.first_name,
				'email':ObjModel.email
			}
			return Response(data)
		serializers = Productos.objects.all().order_by('-id')
		try:
			serializer = ProductosSerializer(serializers, many=True)
		except (TypeError, ValueError) as err:
			print 'ERROR:', err
		return Response(serializer.data)
	def post(self, request, *args, **kwargs):
		ObjModel = Productos()
		ObjModel.name = request.data['name']
		ObjModel.last_name = request.data['last_name']
		ObjModel.first_name = request.data['first_name']
		ObjModel.email = request.data['email']
		ObjModel.save()

		data = {
			'setCod': 0,
		}
		return Response(data)
	def put(self, request, *args, **kwargs):
		Productos.objects.filter(pk=request.data['pk']).update(name=request.data['name'],first_name=request.data['first_name'],last_name=request.data['last_name'],email=request.data['email'])
		data = {
			'setCod': 0,
		}
		return Response(data)
	def delete(self, request, *args, **kwargs):
		post = Productos.objects.get(pk=self.kwargs['pk']).delete()
		data = {
			'setCod': 0,
		}
		return Response(data)									