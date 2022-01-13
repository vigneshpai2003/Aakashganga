from django.shortcuts import render, redirect

from .models import Announcement, Event


def index(request):
    return render(request, "home/index.html", {
        'announcement': Announcement.objects.first(),
        'events': sorted(Event.objects.all().live(), key=lambda x: x.priority)
    })

def team(request):
    return render(request, "home/team.html")

def events(request):
    return render(request, "home/events.html")

def gallery(request):
    return render(request, "home/gallery.html")

def facilities(request):
    return render(request, "home/facilities.html")

def dhruv(request):
    return render(request, "home/dhruv.html")
