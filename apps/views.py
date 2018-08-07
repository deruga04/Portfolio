from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'index.html')

def igbb(req):
    return render(req, 'igbb.html')

def ssl(req):
    return 'zrr-5ptgD5aKNsy-erik3hFivxUFLlmCSvFHI-nrZxY.ZHRLRKR1M7CWxOC4CIh4zK3jYb_Ec94b37iS9CD2DQI'