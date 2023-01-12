from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

def index(request):
    return (request, "singlepageapp/index.html")

texts = ['section1', 'section2', 'section3']

def section(request, section_id):
    if(section_id >= 1 and section_id <= 3):
        return HttpResponse(texts[section_id-1])
    else:
        raise Http404("No such section exists!")