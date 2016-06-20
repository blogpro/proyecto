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
from .models import UserService, Note
from post.models import Post

class User(APIView):
	def post(self, request, *args, **kwargs):
		email_f = request.POST['email']

		ObjModelGet = UserService.objects.filter(email=email_f).count()
		if ObjModelGet == 0:
			ObjUserServicesave = UserService()
			ObjUserServicesave.email = email_f
			ObjUserServicesave.save()
			idu=ObjUserServicesave.save()
			objUser = UserService.objects.get(email=email_f)

			data = {
			'user_id': objUser.id,
			'email': objUser.email,
			}
		else:
			objUser = UserService.objects.get(email=email_f)
			data = {
			'user_id': objUser.id,
			'email': "",
			}	
		return Response(data)
	def get(self, request, *args, **kwargs):
		"""
		Return the user id associated with this session if one exists.
		"""
		ObjUser = UserService.objects.all()
		ObjPostQuery = PostQuery.objects.all()
		SocialArray = list()
		for s in ObjUser:
			SocialArray.append({
			"email": str(s.email),
			})
		return Response(SocialArray)


class Nota(APIView):
	def post(self, request, *args, **kwargs):
		pk_f = request.POST['pk']
		title_f = request.POST['title']
		text_f = request.POST['text']

		objUser = UserService.objects.get(pk=pk_f)
		ObjNotesave = Note()
		ObjNotesave.user = objUser
		ObjNotesave.title = title_f
		ObjNotesave.text = text_f
		ObjNotesave.save()

		objNote = Note.objects.filter(user__id=objUser.id)
		SocialArray = list()
		for s in objNote:
			SocialArray.append({
			"user": str(s.user.email),
			"title": str(s.title),
			"text": str(s.text),
			"fecha": str(s.fecha_registro),
			})
		return Response(SocialArray)

	def get(self, request, *args, **kwargs):
		"""
		Return the user id associated with this session if one exists.
		"""
		objNote = Note.objects.all().order_by('id')
		SocialArray = list()
		for s in objNote:
			SocialArray.append({
			"user": str(s.user.email),
			"title": str(s.title),
			"text": str(s.text),
			"fecha": str(s.fecha_registro),
			})
		return Response(SocialArray)

class NotaDetail(APIView):
	def get(self, request, pk, *args, **kwargs):
		"""
		Return the user id associated with this session if one exists.
		"""
		objNote = Note.objects.filter(user__id=pk).order_by('id')
		SocialArray = list()
		for s in objNote:
			SocialArray.append({
			"user": str(s.user.email),
			"title": str(s.title),
			"text": str(s.text),
			"fecha": str(s.fecha_registro),
			})
		return Response(SocialArray)					