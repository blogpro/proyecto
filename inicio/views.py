from django.shortcuts import render, render_to_response, get_object_or_404,render
from django.template import RequestContext

# Create your views here.
def vw_inicio(request):
	return render_to_response('inicio.html', context_instance=RequestContext(request))

