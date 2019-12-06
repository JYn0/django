from django.shortcuts import render
import json
from datetime import datetime
from urllib.request import urlopen

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def codiWorldcup(request):
    return render(request, 'codi/codiWorldcup.html')

def get_weather(request):
    url = ''
    client_key = ''
    
    return ''