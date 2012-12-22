import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.conf import settings
from django.template import RequestContext
from models import Trip
from forms import TripForm
from django.contrib import messages
from django.core.urlresolvers import reverse


def settings(request, template_name="settings.html"):
    ctx = dict(tab="settings")
    return render_to_response(
        template_name, RequestContext(request, ctx))

def edit(request, trip_id=None, template_name="edit.html"):
    trip = None
    if trip_id:
        try:
            trip = Trip.objects.get(id=trip_id)
        except Trip.DoesNotExist:
            raise Http404

    if request.method == "GET":
        if trip:
            form = TripForm(instance=trip)
        else:
            form = TripForm(initial={'date': datetime.datetime.now().date()})

    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, u"Saved!")
            return HttpResponseRedirect(reverse("log"))
        else:
            messages.error(request, u"Uh oh... Error!")

    ctx = dict(
        trip=trip,
        tab="edit",
        form=form,
        )

    return render_to_response(
        template_name, RequestContext(request, ctx))

def log(request, template_name="log.html"):
    trips = Trip.objects.all()
    ctx = dict(
        tab="log",
        trips=trips,
        )
    return render_to_response(
        template_name, RequestContext(request, ctx))
