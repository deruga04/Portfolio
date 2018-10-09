from django.shortcuts import render
from django.views import generic
import random

# Create your views here.
def index(req):
    return render(req, 'index.html')

def photos(req):
    return render(req, 'photos.html')

# def igbb(generic.ListView):
#     return render(req, 'igbb.html')