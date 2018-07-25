from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    print "AMADON"
    context = {
        "jay": "silent bob"
    }
    return render(request, 'amadon/index.html', context)

def odell(request):
    return HttpResponse("odell catches everything")

def buy1(request):
    print "buying1"
    print request.POST
    print request.POST['quantity']
    quan = request.POST['quantity']
    print "You bought " + quan + " lambo(s)"
    price = 219780
    quanti = int(quan)
    total = price * quanti
    fixed_total = price * quanti
    print "Your total is: "
    print total
    request.session['quantity'] = quanti
    request.session['car'] = "lambo"
    if not 'total' in request.session:
        request.session['total'] = 0
    request.session['total'] += total
    request.session['fixed_total'] = total
    if not 'items' in request.session:
        request.session['items'] = 0
    request.session['items'] += quanti
    return redirect('/amadon/checkout/')

def buy2(request):
    print "buying2"
    print request.POST
    print request.POST['quantity']
    quan = request.POST['quantity']
    print "You bought " + quan + " aston martins(s)"
    price = 198995
    quanti = int(quan)
    total = price * quanti
    fixed_total = total
    print "Your total is: "
    print total
    request.session['quantity'] = quanti
    request.session['car'] = "DB11"
    if not 'total' in request.session:
        request.session['total'] = 0
    request.session['total'] += total
    request.session['fixed_total'] = fixed_total
    if not 'items' in request.session:
        request.session['items'] = 0
    request.session['items'] += quanti
    return redirect('/amadon/checkout/')

def checkout(request):
    context = {
        "jay": "silent bob",
        "quantity": request.session['quantity'],
        "car": request.session['car'],
        "total": request.session['total'],
        "fixed": request.session['fixed_total'],
        "items": request.session['items']
    }
    return render(request, 'amadon/checkout.html', context)

def clear(request):
    print "clearing"
    print request.session['total']
    request.session['total'] = 0
    print request.session['total']
    request.session['items'] = 0
    return redirect('/amadon/')
# Blueprint vvv

def yourMethodFromUrls(request):
  context = {
  "somekey":"somevalue"
  }
  return render(request,'appname/page.html', context)

# Blueprint ^^^

