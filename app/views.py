from __future__ import print_function

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from app.models import User, Todo
from forms import SignUpForm


def main_page(request):
    if 'user_id' in request.session:
        user_obj = User.objects.filter(id=request.session['user_id'])
        todo_obj = Todo.objects.filter(user_id=request.session['user_id'])
        data = RequestContext(request, {'name': request.session['name'], 'user': user_obj, 'todo': todo_obj})

        return render_to_response('todo_list.html',
                                  {'name': request.session['name'], 'user': user_obj, 'todo': todo_obj},
                                  context_instance=RequestContext(request),)
    else:
        form = SignUpForm()

        return render_to_response('index.html', {'form': form}, context_instance=RequestContext(request),)


def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            obj = form.save()
            id = obj.id
            request.session['user_id'] = id
            request.session['name'] = form.cleaned_data['name']

        return HttpResponseRedirect('/')


def signIn(request):
    user_obj = User.objects.filter(email=request.POST.get('email'), password=request.POST.get('password'))
    if user_obj.count():
        request.session['user_id'] = user_obj[0].id
        request.session['name'] = user_obj[0].name
        request.session.modified = True

    return HttpResponseRedirect('/')


def signOut(request):
    del request.session['user_id']
    del request.session['name']
    request.session.modified = True

    return HttpResponseRedirect('/')
