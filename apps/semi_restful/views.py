from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import User

def index(request):
    print "Semi Restful Users"
    print User.objects.all()
    context = {
        "jay": "silent bob3",
        "user1": User.objects.first(),
        "users": User.objects.all()
    }
    return render(request, 'semi_restful/index.html', context)

def new(request):
    print "new user form"
    return render(request, 'semi_restful/new.html')

def create(request):
    print "creating new user"
    print request.POST
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect("/semi_restful/")

def show(request, user_id):
    print "Showing off"
    print user_id
    context = {
        "user": User.objects.get(id=user_id)
    }
    return render(request, 'semi_restful/show.html', context)

def edit(request, user_id):
    print "editing"
    print user_id
    context = {
        "user": User.objects.get(id=user_id)
    }
    return render(request, 'semi_restful/edit.html', context)

def delete(request, user_id):
    print "deleting"
    print user_id
    x = User.objects.get(id=user_id)
    x.delete()
    return redirect('/semi_restful/')

def update(request, user_id):
    print "updating"
    print user_id
    y = User.objects.get(id=user_id)
    print y
    print y.first_name
    print request.POST
    print request.POST['first_name']
    y.first_name = request.POST['first_name']
    y.last_name = request.POST['last_name']
    y.email = request.POST['email']
    y.save()
    return redirect('/semi_restful/')
def odell(request):
    return HttpResponse("odell catches everything")

def yourMethodFromUrls(request):
  context = {
  "somekey":"somevalue"
  }
  return render(request,'appname/page.html', context)

# Blueprint ^^^

