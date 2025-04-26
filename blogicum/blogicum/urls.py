"""
URL configuration for blogicum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Examples:
    Function views:
        1. Add an import: from my_app import views
        2. Add a URL: path('', views.home, name='home')
    
    Class-based views:
        1. Add an import: from other_app.views import Home
        2. Add a URL: path('', Home.as_view(), name='home')
    
    Including another URLconf:
        1. Import include(): from django.urls import include, path
        2. Add a URL: path('blog/', include('blog.urls'))
"""
from django.urls import include, path


app_name = 'blogicum'

urlpatterns = [
    # Blog app routes
    path('', include('blog.urls', namespace='blog')),
    
    # Pages app routes
    path('pages/', include('pages.urls', namespace='pages')),
]