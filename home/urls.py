from django import urls
from django.urls import path,include,re_path

from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('universitiesdb',views.universitiesdb,name='universitiesdb'),
    path('addtojson',views.addtojson,name='addtojson'),
    path('collegedetails',views.collegedetails,name='collegedetails')
]
