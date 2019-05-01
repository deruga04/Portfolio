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

def handler404(request, *args, **argv):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response
    
# class PhotoListView(generic.ListView):
#     model = Photo
#     context_object_name = 'photo_list'
#     queryset = Photo.objects
#     template_name = 'photos.html'

def projects(request):
    projects = Project.objects
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context=context)

def acme(request):
    return 'pCcUIubCdKXn-OsGPbVA81vU8LZwqKnzakNRESpAF74.stJdK5-9wB6luidbkIffaMMfstLUFigaPbNn-Jb36uM'

# def igbb(generic.ListView):
#     return render(req, 'igbb.html')
