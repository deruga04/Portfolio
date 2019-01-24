from django.shortcuts import render
from django.views import generic
from apps.models import Project

# Create your views here.
def index(req):
    return render(req, 'index.html')

def cert(req):
    return render(req, 'cert.html')

# class PhotoListView(generic.ListView):
#     model = Photo
#     context_object_name = 'photo_list'
#     queryset = Photo.objects
#     template_name = 'photos.html'

class ProjectListView(generic.ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projects.html'


# def igbb(generic.ListView):
#     return render(req, 'igbb.html')
