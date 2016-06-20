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

from post.models import Post

from service.serializers import PostQuerySerializer

class ServicePostQuery(APIView):
	def get(self, request, *args, **kwargs):
		"""
		Return the user id associated with this session if one exists.
		"""
		serializers = Post.objects.all().order_by('-id')
		try:
			serializer = PostQuerySerializer(serializers, many=True)
		except (TypeError, ValueError) as err:
			print 'ERROR:', err
		return Response(serializer.data)