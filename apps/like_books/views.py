from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print "Like books"
    context = {
        "jay": "silent bob2",
        # "book1": Book.objects.first()
    }
    return render(request, 'like_books/index.html', context)

def odell(request):
    return HttpResponse("odell catches everything")

def yourMethodFromUrls(request):
  context = {
  "somekey":"somevalue"
  }
  return render(request,'appname/page.html', context)

# Blueprint ^^^

