from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    print "NINJA GOLD BABY"
    print request.session['gold_now']
    context = {
        "jay": "silent bob",
        "total_gold": request.session['gold'],
        "gold_now": request.session['gold_now']
    }
    return render(request, 'gold/index.html', context)

def process(request, location):
    print 'processing'
    print location
    if location == 'farm':
        print "You stole 10-20 gold"
        gold = random.randrange(10,21)
        print gold

    if location == 'cave':
        print "You stole 5-10 gold"
        gold = random.randrange(5,11)
        print gold
    if location == 'house':
        print "You stole 2-5 gold"
        gold = random.randrange(2,6)
        print gold
    if location == 'casino':
        print "You won or lost up to 50 gold"
        gold = random.randrange(-50,51)
        print gold

    print "Gold is", gold

    if not 'gold' in request.session:
        request.session['gold'] = 0
    request.session['gold'] += gold
    request.session['gold_now'] = gold

    print request.session['gold'], "is your total gold"
    print request.session['gold_now'], "gold added"

    return redirect('/gold/')

def odell(request):
    return HttpResponse("odell catches everything")


# Blueprint vvv

def yourMethodFromUrls(request):
  context = {
  "somekey":"somevalue"
  }
  return render(request,'appname/page.html', context)

# Blueprint ^^^

