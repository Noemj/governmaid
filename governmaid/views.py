from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404


def home(request, *args, **kwargs):
    return render(request, kwargs['template'],{'extension':'template.html'})

@login_required
def hello(request, **kwargs):
	return HttpResponse("Welcome, "+request.user.username+"!<br /><a href='/logout'>Logout</a>")

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def login(request, **kwargs):
	


	if request.user.is_authenticated():
		return HttpResponseRedirect('/hello/')
	if request.METHOD=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user = auth.authenticate(username=username, password=password)
		auth.login(request, user)
		return HttpResponseRedirect('/hello/')
	else:
		return render(request, kwargs['template'],{'extension':'template.html'})
