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
from django.contrib.auth.decorators import login_required


@login_required
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
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.user = request.user
            trip.save()
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

@login_required
def log(request, template_name="log.html"):
    try:
        trips = Trip.objects.filter(user=request.user)
    except Exception, e:
        print e
        import pdb; pdb.set_trace()

    ctx = dict(
        tab="log",
        trips=trips,
        totalmiles=sum(trip.distance() for trip in trips)
        )
    return render_to_response(
        template_name, RequestContext(request, ctx))

@login_required
def email(request, template_name="email.html"):
    ctx = dict()
    if request.method == "POST":
        print request.POST
        email = request.POST.get("email", "your mom")
        messages.info(request, "sent an email to: %s" % email)
        return HttpResponseRedirect(reverse("log"))

    return render_to_response(
        template_name, RequestContext(request, ctx))
