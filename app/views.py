from __future__ import print_function

from datetime import datetime

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from app.models import User, Todo
from forms import SignUpForm
import json


def main_page(request):
    if request.user.is_authenticated():
        # TODO: show todolist
        todoList = Todo.objects.filter(author_id=request.user.id, completed=False)
        return render_to_response('todo_list.html',
                                  {'todoList': todoList, 'user': request.user},
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
            redirect_to = request.GET.get('next')

            return HttpResponseRedirect(redirect_to)
    else:
        form = SignUpForm()

    return render_to_response('signUp.html', {'form': form}, context_instance=RequestContext(request))


def addTodo(request):
    if request.method == 'POST':
        response_data = {}
        jobText = request.POST.get('job')
        deadline = request.POST.get('deadline')
        # todo = Todo.objects.create(todo_job=jobText, author=request.user,
        #                           deadline_date=datetime.strptime(deadline, "%Y-%m-%d").date())
        response_data['job_text'] = jobText
        response_data['deadline'] = deadline
        response_data['todo_id'] = 3

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def deleteTodo(request):
    if request.method == 'POST':
        response_data = {'status': 'OK'}
        todo_id = request.POST.get('id')
        #try:
        #    Todo.objects.get(id=todo_id).delete()
        #    response_data['status'] = 'OK'
        #except Todo.DoesNotExist:
        #    response_data['status'] = 'BAD'

        return HttpResponse(json.dumps(response_data), content_type="application/json")
