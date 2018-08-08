from django.shortcuts import render
import random

# Create your views here.
def index(req):
    greetings = ["Hello MTV, welcome to my crib!", "안녕하세요", "Nice to meet 'cha", "Welcome"]

    return render(req, 'index.html', context={"greeting": random.choice(greetings)})


def igbb(req):
    return render(req, 'igbb.html')

def ssl(req):
    return render(req, 'acme')