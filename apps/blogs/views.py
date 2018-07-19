from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse('placeholder to later display all the list of blogs')

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    return redirect('/blogs')

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
