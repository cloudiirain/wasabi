from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib import auth

from forms import MyRegistrationForm

def home(request):
    return render(request, 'index.html')
"""
def login(request):

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))

def register(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = MyRegistrationForm()
    return render(request, "register.html", {
        'form': form,
    })
"""

def dashboard(request):
    pass
