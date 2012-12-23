from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

def login(request, template_name="registration/login.html"):
    ctx = dict()
    print request.POST
    return render_to_response(
        template_name, RequestContext(request, ctx))
