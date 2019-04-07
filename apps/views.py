from django.shortcuts import render
from django.views import generic
from apps.models import Project
import requests

# Create your views here.
def index(req):
    r = requests.get('http://quotes.rest/qod').json()
    
    # quote = r['contents']
    # quote_author = ''

    try:
        quote = r['contents']['quotes'][0]['quote']
        quote_author = r['contents']['quotes'][0]['author']
    except KeyError:
        quote = 'You miss 100% of the shots you don\'t take - Wayne Gretzky'
        quote_author = 'Michael Scott'

    context = {
        'quote': quote,
        'quote_author': quote_author,
    }

    return render(req, 'index.html', context=context)

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
