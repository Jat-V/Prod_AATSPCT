from django.shortcuts import render
from datetime import date
from events.models import Event


def index(request):
    today_l = date.today().strftime("%B %d, %Y")
    active_events = Event.objects.filter(Active_check=True)
    contex = {'nav_uri_I': 'active',
              'date': today_l,
              'active_events': active_events,
              }
    return render(request, "index.html", contex)


def about(request):
    contex = {'nav_uri_A': 'active'}
    return render(request, "about.html", contex)


def conference(request):
    contex = {'nav_uri_C': 'active'}
    return render(request, "conference.html", contex)


def gallery(request):
    contex = {'nav_uri_G': 'active'}
    return render(request, "gallery.html", contex)
