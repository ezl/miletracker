from django.template import RequestContext
from django.contrib import messages
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from models import UserProfile
from forms import UserProfileForm

def logout(request):
    response = auth_logout(request)
    messages.info(request, "Thanks for using Mile Tracker today! Come back soon.")
    return HttpResponseRedirect(reverse("landing"))

@login_required
def settings(request, template_name="settings.html"):
    formclass = UserProfileForm
    userprofile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "GET":
        form = formclass(instance=userprofile)
    if request.method == "POST":
        # import pdb; pdb.set_trace()
        form = formclass(request.POST, instance=userprofile)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.user = request.user
            userprofile.save()
            messages.success(request, "Your settings were successfully saved.")
        else:
            messages.error(request, "Error.")

    ctx = dict(
        tab="settings",
        form=form,
        )
    return render_to_response(
        template_name, RequestContext(request, ctx))

def login(request, template_name="registration/login.html"):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get("username", "").lower()
        password = request.POST.get("password", "")
        print "username: %s" % username
        print "password: %s" % password

        """
        import pdb; pdb.set_trace()
        """
        username = request.POST.get("username", "").lower()
        password = request.POST.get("password", "")
        if username and password:
            try:
                user = User.objects.get(username__iexact=username)
            except User.DoesNotExist:
                user = None

            if user:
                print "user exists"
                response = auth_login(request)
                return response
            else:
                print "no such user, create it"
                usercreationform = UserCreationForm({
                    'username': username,
                    'password1': password,
                    'password2': password,
                    })
                print "print creation form is valid", usercreationform.is_valid()
                if usercreationform.is_valid():

                    usercreationform.save()
                    response = auth_login(request)
                    return response
                else:
                    pass
                    print "invald registration, but valid login?"
        else:
            print "invalid login form"
            print "hi"
            form = AuthenticationForm(data=request.POST)
            form.is_valid() # just doing this to get the errors to trigger
            # import pdb; pdb.set_trace()

    # form = AuthenticationForm()
    ctx = dict(form=form)
    print form.errors
    # if form.errors:
    #     messages.error(request, "Oops, we had a problem logging you in. Can you try again?")
    return render_to_response(
        template_name, RequestContext(request, ctx))
