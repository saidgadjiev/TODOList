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
        response_data = []
        todoList = Todo.objects.filter(author_id=request.user.id).order_by('-created_date')
        now = datetime.now().date()
        for todo in todoList:
            todo_data = {}
            todo_data['todo_data'] = todo
            old = todo.deadline_date
            todo_data['overdude'] = old < now
            response_data.append(todo_data)

        return render_to_response('todo_list.html',
                                  {'todoList': response_data, 'user': request.user},
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
        job_text = request.POST.get('job')
        deadline = request.POST.get('deadline')
        todo = Todo.objects.create(todo_job=job_text, author=request.user,
                                   deadline_date=datetime.strptime(deadline, "%Y-%m-%d").date())
        response_data['job_text'] = job_text
        response_data['deadline'] = deadline
        response_data['todo_id'] = todo.id
        now = datetime.now().date()
        curr_date = datetime.strptime(deadline, "%Y-%m-%d").date()
        response_data['overdude'] = curr_date < now

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def deleteTodo(request):
    if request.method == 'POST':
        response_data = {'status': 'OK'}
        todo_id = request.POST.get('id')
        try:
            Todo.objects.get(id=todo_id).delete()
            response_data['status'] = 'OK'
        except Todo.DoesNotExist:
            response_data['status'] = 'BAD'

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def completeTodo(request):
    if request.method == 'POST':
        response_data = {}
        todo_id = request.POST.get('id')
        todo = Todo.objects.get(id=todo_id)
        todo.completed = not todo.completed
        response_data['complete'] = todo.completed
        todo.save()

        return HttpResponse(json.dumps(response_data), content_type="application/json")
