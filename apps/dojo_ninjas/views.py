from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print "AMADON"
    context = {
        "jay": "silent bob"
    }
    return render(request, 'amadon/index.html', context)

def odell(request):
    return HttpResponse("odell catches everything")

def yourMethodFromUrls(request):
  context = {
  "somekey":"somevalue"
  }
  return render(request,'appname/page.html', context)

# Blueprint ^^^

