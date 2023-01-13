from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

def index(request):
    return render(request, "singlepageapp/index.html")

texts = ['This section 1 is about watching Tehran, its latest season and getting to witness what , in the last AMA, Bill Gates Talked about , `suspensful` ', 'Well, this section doesn\'t have much to be thought about but i do think we will be getting some serious content from this season', 'this whole section is just WTFFFF!', 'Tis is the Final section about getting OK and not getting subdued about becoming something or the other..']

def section(request, section_id):
    if(section_id >= 1 and section_id <= 4):
        return HttpResponse(texts[section_id-1])
    else:
        raise Http404("No such section exists!")