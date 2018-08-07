from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('igbb/',views.igbb, name='igbb'),
    path('.well-known/acme-challenge/zrr-5ptgD5aKNsy-erik3hFivxUFLlmCSvFHI-nrZxY', views.ssl, name='acme'),
]