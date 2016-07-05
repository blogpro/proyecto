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
		serializers = Categoria.objects.all().order_by('-id')
		try:
			serializer = CategoriasSerializer(serializers, many=True)
		except (TypeError, ValueError) as err:
			print 'ERROR:', err
		return Response(serializer.data)
	def post(self, request, format=None):
		serializer = CategoriasSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)			