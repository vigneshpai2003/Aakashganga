from django.urls import path
from . import views

urlpatterns = [
    path('', views.aakashvani, name="aakashvani"),
]