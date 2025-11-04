from django.conf import settings
from django.shortcuts import render
from django.http import FileResponse
import plotly.express as px

def home(request):

    return render(request, 'website/home.html')