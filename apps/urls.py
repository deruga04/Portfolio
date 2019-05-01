from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    # path('igbb/',views.igbbView.as_view(), name='igbb'),
    path('.well-known/acme-challenge/pCcUIubCdKXn-OsGPbVA81vU8LZwqKnzakNRESpAF74', views.acme, name='acme')
]
