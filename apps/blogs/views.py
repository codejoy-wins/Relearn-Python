from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'blogs/index.html')
    return HttpResponse('placeholder to later display all the list of blogs')

def new(request):
    return render(request, 'blogs/new.html')

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
        return redirect("/blogs/")
    else:
        return redirect("/blogs/")

def show(request, number):
    return HttpResponse('placeholder for blog number: ' + number )

def show_word(request, word):
    return HttpResponse('placeholdr for blog word: ' + word)

def edit(request, number):
    return HttpResponse('placeholder for editing ' + number)

def destroy(request, number):
    print ('destroying blog number: ' + number)
    return redirect('/blogs')

def odell(request):
    return HttpResponse("odell catches everything")
