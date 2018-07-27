from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print "USER LOGIN"
    context = {
        "jay": "silent bob"
    }
    return render(request, 'user_login/index.html', context)

def odell(request):
    return HttpResponse("odell catches everything")

# Blueprint vvv

def yourMethodFromUrls(request):
  context = {
  "somekey":"somevalue"
  }
  return render(request,'appname/page.html', context)

# Blueprint ^^^

