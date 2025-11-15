from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("cv/", views.cv, name="cv"),
    path("projects/", views.projects, name="projects"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]