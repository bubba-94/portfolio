from django.conf import settings
from django.shortcuts import render
from django.http import FileResponse
import plotly.express as px

def home(request):
    # Sample skills chart
    skills = ["Python", "Django", "Docker", "Git"]
    proficiency = [90, 80, 70, 85]

    fig = px.bar(
        x=skills, 
        y=proficiency, 
        labels={"x":"Skill", "y":"Proficiency (%)"}, 
        title="Skills")
    
    graph_html = fig.to_html(full_html=False)

    context = {
        "graph_html": graph_html,
        "profile_image": "images/profile.jpg",  # Place your image in static/cv_app/images/
    }
    return render(request, 'cv_app/home.html', context)