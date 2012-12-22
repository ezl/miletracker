from django.shortcuts import render_to_response, get_object_or_404
from django.conf import settings
from django.template import RequestContext
from forms import TripForm

# from django.contrib import messages


def settings(request, template_name="settings.html"):
    ctx = dict(tab="settings")
    return render_to_response(
        template_name, RequestContext(request, ctx))

def edit(request, template_name="edit.html"):
    if request.method == "POST":
        print request.POST

    form = TripForm()
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
