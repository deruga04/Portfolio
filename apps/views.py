from django.shortcuts import render
from django.views import generic
import random

# Create your views here.
def index(req):
    greetings = ["Hello MTV, welcome to my crib!", "안녕하세요!", "Nice to meet 'cha", "Welcome"]

    return render(req, 'index.html', context={"greeting": random.choice(greetings)})


# def igbb(generic.ListView):
#     return render(req, 'igbb.html')