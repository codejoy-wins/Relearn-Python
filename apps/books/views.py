from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'books/index.html')
    return HttpResponse('placeholder to later display all the list of books')

def new(request):
    return HttpResponse('placeholder to display a new form to create a new book')

def create(request):
    return redirect('/books/')

def show(request, number):
    return HttpResponse('placeholder for book number: ' + number )

def show_word(request, word):
    return HttpResponse('placeholdr for book word: ' + word)

def edit(request, number):
    return HttpResponse('placeholder for editing book ' + number)

def destroy(request, number):
    print ('destroying book number: ' + number)
    return redirect('/books/')

def odell(request):
    return HttpResponse("odell catches every book")