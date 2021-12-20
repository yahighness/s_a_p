from django.shortcuts import render

 

from django.shortcuts import render, get_object_or_404, redirect
from .models import 
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EditorForm, CommentForm
# Create your views here.


def home(request):
    return render(request, 'home.html')


def client(request):
    return render(request, 'client.htm')

def resource(request):
    return render(request, 'resoure.html')

def blog(request):
    return render(request, 'blog.html')


