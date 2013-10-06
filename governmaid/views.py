from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from postapp.models import Post


def home(request, *args, **kwargs):
	return render(request, kwargs['template'],{'extension':'template.html'})

def city(request, *args, **kwargs):
	posts_time = Post.objects.order_by('score')

	return render(request, kwargs['template'],{'extension':'template.html'})

def city(request, *args, **kwargs):
	posts = Post.objects.order_by('score')[:10]
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
	if request.method == "POST":
		username=request.POST['username']
		password=request.POST['password']
		user = auth.authenticate(username=username, password=password)
		auth.login(request, user)
		return HttpResponseRedirect('/hello/')
		cities= City.objects.()
	else:
		return render(request, kwargs['template'],{'extension':'template.html'})
