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


from django.core.urlresolvers import reverse

from categorias.models import Categoria
from post.models import Post

from .serializers import PostQuerySerializer, CategoriasSerializer

class ServicePostQuery(APIView):
	def get(self, request, *args, **kwargs):
		serializers = Post.objects.all().order_by('-id')
		try:
			serializer = PostQuerySerializer(serializers, many=True)
		except (TypeError, ValueError) as err:
			print 'ERROR:', err
		return Response(serializer.data)

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
		data = {
			'setCod': request.data,
		}
		return Response(data)