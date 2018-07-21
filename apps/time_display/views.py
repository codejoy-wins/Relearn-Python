from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
  context = {
  "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
  "jay": "silent bob"
  }
  return render(request,'time_display/index.html', context)

def new(request):
    return render(request, 'time_display/new.html')

def create(request):
    print 'creating'
    if request.method == "POST":
        print "*"*50
        print request.method + " is request dot method"
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"
        print "*"*50
        return redirect("/time_display/")
    else:
        return redirect("/time_display/")

def show(request, number):
    return HttpResponse('placeholder for blog number: ' + number )

def show_word(request, word):
    return HttpResponse('placeholdr for blog word: ' + word)

def edit(request, number):
    return HttpResponse('placeholder for editing ' + number)

def destroy(request, number):
    print ('destroying blog number: ' + number)
    return redirect('/time_display')

# Blueprint vvv

def yourMethodFromUrls(request):
  context = {
  "somekey":"somevalue"
  }
  return render(request,'appname/page.html', context)

# Blueprint ^^^

def odell(request):
    return HttpResponse("odell catches everything")