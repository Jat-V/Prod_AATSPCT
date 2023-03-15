from django.shortcuts import render
from .models import Event


def index(request):
    active_events = Event.objects.filter(Active_check=True)
    context = {
        "nav_uri_E": "active",
        "active_events": active_events,
    }
    return render(request, "events.html", context)


# def cal(request):
#    return render(request, "calendar.html")


def ev_desc(request, spec_event_id):
    try:
        specific_event = Event.objects.get(pk=spec_event_id)
    except Event.DoesNotExist:
        raise Http404("Event does not exist. Go Back.")

    contex = {
        "specific_event": specific_event,
    }
    return render(request, "ev_base.html", contex)

