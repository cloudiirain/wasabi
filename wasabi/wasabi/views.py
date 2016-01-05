from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from collections import OrderedDict
from directory.models import Chapter
from forms import ChapterForm

def home(request):
    return render(request, 'index.html')

@sensitive_post_parameters()
@csrf_protect
def login(request):
    redirect_to = reverse('dashboard')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(redirect_to)
    else:
        form = AuthenticationForm(request)
    return render(request, 'registration/login.html', { 'form': form, 'next': redirect_to,})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required()
def dashboard(request):
    # get chapters related to User
    chapters = Chapter.objects.filter(owner=request.user).order_by('series__title')
    series = OrderedDict()
    for chapter in chapters:
        if not chapter.series in series:
            series[chapter.series] = []
        series[chapter.series].append(chapter)
    return render(request, 'dashboard.html', { 'series' : series })

@login_required()
def chapter(request, pk=None):
    if request.method == "POST":
        form = ChapterForm(request.POST)
        if form.is_valid():
            if pk == None:
                form.save()
            else:
                chapter = get_object_or_404(Chapter, pk=pk)
                form = ChapterForm(request.POST, instance=chapter)
                form.save()
            return HttpResponseRedirect(reverse('dashboard'))
    if pk != None:
        chapter = get_object_or_404(Chapter, pk=pk)
        form = ChapterForm(instance=chapter)
    else:
        form = ChapterForm()
    return render(request, 'chapter.html', { 'form': form })


class ChapterCreate(CreateView):
    model = Chapter
    template_name = 'chapter.html',
    form_class = ChapterForm
    fields = ['title', 'series', 'owner', 'order', 'body']

    def dispatch(self, *args, **kwargs):
        return super(ChapterCreate, self).dispatch(*args, **kwargs)

class ChapterUpdate(UpdateView):
    model = Chapter
    template_name = 'chapter.html',
    form_class = ChapterForm,
    fields = ['title', 'series', 'owner', 'order', 'body']

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.object.owner:
            return HttpResponseRedirect(reverse('dashboard'))
        return super(ChapterUpdate, self).dispatch(*args, **kwargs)

"""
class ChapterDelete(DeleteView):
    model = Chapter

    def dispatch(self, *args, **kwargs):
        return super(ChapterDelete, self).dispatch(*args, **kwargs)
"""