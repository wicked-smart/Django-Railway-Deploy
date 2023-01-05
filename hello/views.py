from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Testing sqlite3 in devellopemnt mode vs postgress in roduction mode!")
