from xml.etree.ElementInclude import include
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "nickscafeapp/home.html")


