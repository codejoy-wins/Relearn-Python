from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime, localtime
# This whole thing broke for some reason
# ADD TIME
def index(request):
    if 'color_now' in request.session:
        print request.session['color_now']
        if request.session['color_now'] == "green":
            print "green logic"
            logic = "gained"
        else:
            print "red logic"
            logic = "lost"
# do some if nots here to maybe fix everything
    context = {
        "jay": "silent bob",
        # "total_gold": request.session['gold'],
        # "gold_now": request.session['gold_now'],
        # "my_color": request.session['color_now'],
        # "my_logic": logic,
        # "created_at": strftime("%I:%M:%S %p, %b %d, %Y", localtime())
    }
    return render(request, 'gold/index.html', context)

def process(request, location):
    print 'processing'
    print location
    color = "green"
    if location == 'farm':
        gold = random.randrange(10,21)

    if location == 'cave':
        gold = random.randrange(5,11)
    if location == 'house':
        gold = random.randrange(2,6)
    if location == 'casino':
        gold = random.randrange(-50,51)
        if gold <0:
            color = "red"

    print "Gold is", gold
    print "Color is", color

    if not 'gold' in request.session:
        request.session['gold'] = 0
    request.session['gold'] += gold
    request.session['gold_now'] = gold
    request.session['color_now'] = color

    print request.session['gold'], "is your total gold"
    print request.session['gold_now'], "gold added"
    print request.session['color_now'], "color now"

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