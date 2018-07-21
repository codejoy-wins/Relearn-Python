from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def odell(request):
    return render(request, 'standard/index.html')
