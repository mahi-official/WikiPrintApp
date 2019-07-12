from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('services/', views.ServiceView, name='services'),
    path('about/', views.AboutView, name='about'),
    path('contact/', views.ContactView, name='contact'),
    path('home/', views.IndexView, name='home'),
    path('projects/', views.ProjectView, name='projects'),
]

