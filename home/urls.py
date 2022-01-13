from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('team', views.team, name="team"),
    path('events', views.events, name="events"),
    path('gallery', views.gallery, name="gallery"),
    path('facilities', views.facilities, name="facilities"),
    path('dhruv', views.dhruv, name="dhruv"),
]