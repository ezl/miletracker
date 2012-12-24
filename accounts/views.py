from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

from django.contrib.auth.views import login as auth_login
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def login(request, template_name="registration/login.html"):
    if request.method == "POST":
        username = request.POST.get("username", "").lower()
        password = request.POST.get("password", "")

        try:
            user = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            user = None

        if user:
            response = auth_login(request)
            return response
        else:
            # create that sucker
            print "5"*50
            #return HttpResponseRedirect(reverse("log"))

    ctx = dict()
    return render_to_response(
        template_name, RequestContext(request, ctx))
