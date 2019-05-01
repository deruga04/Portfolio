from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    # path('igbb/',views.igbbView.as_view(), name='igbb'),
    path('.well-known/acme-challenge/o5UI5142SDnOUsgJ3l9TLUfB6_dFE0ipBLqk5xRXRYE', views.acme, name='acme')
]
