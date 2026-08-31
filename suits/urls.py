
from django.urls import path
from . import views
from .views import armor_detail, technology_detail

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('armor/', views.armor,name='armor'),
    path('technology/', views.technologies,name='technology'),
    path('actor/', views.actor,name='actor'),
    path('armor/<int:id>/', armor_detail, name='armor_detail'),
    path('technology/<int:id>/', technology_detail, name='technology_detail'),
    path('history/', views.history, name='history'),
    path('archive/', views.archive, name='archive'),
   
]