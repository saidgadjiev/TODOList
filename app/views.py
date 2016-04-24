from __future__ import print_function

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from app.models import User, Todo
from forms import SignUpForm


def main_page(request):
    if request.user.is_authenticated():

        return render_to_response('todo_list.html',
                                  {'name': request.user.username, 'user': request.user},
                                  context_instance=RequestContext(request))
    else:
        return render_to_response('index.html', context_instance=RequestContext(request))


def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            User.objects.create_user(username, email, password)
            user = authenticate(username=username, password=password)
            login(request, user)

            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()

    return render_to_response('signUp.html', {'form': form}, context_instance=RequestContext(request))
