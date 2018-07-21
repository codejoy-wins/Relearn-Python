from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    rando = get_random_string(length=14)
    print rando
    if (not 'count' in request.session):
        request.session['count'] = 1
        count = request.session['count']
    context = {
        "rando": rando,
        "count": request.session['count']
    }
    return render(request, 'random_word/index.html', context)

def reset(request):
    print "resetting"
    request.session.clear()
    #clear session or set counter to 0
    return redirect('/random_word/')

def generate(request):
    print "generating!!!!!!!"
    random = get_random_string(length=14)
    print random
    request.session['random'] = random
    request.session['count'] = request.session['count']+1
    return redirect('/random_word/')

def new(request):
    return render(request, 'random_word/new.html')

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
        return redirect("/random_word/")
    else:
        return redirect("/random_word/")

def show(request, number):
    return HttpResponse('placeholder for blog number: ' + number )

def show_word(request, word):
    return HttpResponse('placeholdr for blog word: ' + word)

def edit(request, number):
    return HttpResponse('placeholder for editing ' + number)

def destroy(request, number):
    print ('destroying blog number: ' + number)
    return redirect('/random_word')

def odell(request):
    return HttpResponse("odell catches everything")

# Blueprint vvv

def yourMethodFromUrls(request):
  context = {
  "somekey":"somevalue"
  }
  return render(request,'appname/page.html', context)

# Blueprint ^^^

