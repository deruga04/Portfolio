from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'index.html')

def projects(req):
    return render(req, 'igbb.html')