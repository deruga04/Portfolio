from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'index.html')

def igbb(req):
    return render(req, 'igbb.html')

def ssl(req):
    return render(req, 'acme')