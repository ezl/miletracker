import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.conf import settings
from django.template import RequestContext
from forms import TripForm
from django.contrib import messages
from django.core.urlresolvers import reverse


def settings(request, template_name="settings.html"):
    ctx = dict(tab="settings")
    return render_to_response(
        template_name, RequestContext(request, ctx))

def edit(request, template_name="edit.html"):
    if request.method == "GET":
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
        tab="edit",
        form=form,
        )

    return render_to_response(
        template_name, RequestContext(request, ctx))

def log(request, template_name="log.html"):
    ctx = dict(tab="log")
    return render_to_response(
        template_name, RequestContext(request, ctx))
