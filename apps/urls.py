from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('photos/', views.PhotoListView.as_view(), name='photos'),
    path('.well-known/acme-challenge/3adLF_0NPSR3IC0zKvG4zH0iU6Xf0-3wf6u7sMPO7OY', views.cert,
            name='cert'),
    # path('igbb/',views.igbbView.as_view(), name='igbb'),
]
