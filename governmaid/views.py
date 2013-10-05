from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

def home(request, *args, **kwargs):
    
    return render(request, kwargs['template'],{'extension':'template.html'})