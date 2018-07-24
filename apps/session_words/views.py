from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

def index(request):
    return render(request, 'session_words/index.html')

# Smart Tim

def process(request):
    new_word = {} # creating an empty dictionary to store entries as objects
    if not 'word' in request.POST: #if no word is entered then redirect 
        return redirect('/session_words/')
    else:
        new_word['word'] = request.POST['word']  
        if not 'color' in request.POST:
            new_word['color'] = "black"
        elif request.POST['color'] == "red":
            new_word['color'] = "red"
        elif request.POST['color'] == "green":
            new_word['color'] = "green"
        elif request.POST['color'] == "blue":
            new_word['color'] = "blue"
        if not 'big_fonts' in request.POST:
            new_word['font_size'] = "p"
        else:
            new_word['font_size'] = "h2"
        new_word['created_at'] = strftime("%I:%M:%S %p, %b %d, %Y", localtime())
        # Append new word to word list
        if not 'word_list' in request.session:
            request.session['word_list'] = []
            request.session['word_list'].append(new_word)
        else:
            word_list = request.session['word_list']
            word_list.append(new_word)
            request.session['word_list'] = word_list
        print "Session added."
        print "Word List:"
        print request.session['word_list']
        for x in request.session['word_list']:
            print x
        return redirect('/session_words/')

def clear(request):
    print "CLEAR"
    if 'word_list' in request.session:
        del request.session['word_list']
    if 'new_word' in request.session:
        del request.session['new_word']
    if 'animal_list' in request.session:
        del request.session['animal_list']
    print "Session cleared."
    return redirect('/session_words/')

# learning Max

def animal(request):
    return render(request, "session_words/animal.html")

def jungle(request):
    print "In the jungle, baby."
    print "*"*44
    print request.POST
    print "*"*44
    # got data.

    animal = {
        'species' : 'not specified',
        'size' : 'not specified',
        'fly' : 'cannot',
        'walk' : 'cannot',
        'swim' : 'cannot',
    }
    variable = bool(request.POST['species'])
    if variable == False:
        print 'no species given'
        return redirect('/session_words/animal/')
    else:
        print ("Your animal is of the species: " + request.POST['species'])
    animal['species'] = request.POST['species']
    if not 'size' in request.POST:
        print 'size not selected'
    else:
        animal['size'] = request.POST['size']
        if request.POST['size'] == 'small':
            print "Your animal is small"
        elif request.POST['size'] == 'medium':
            print "Your animal is medium sized"
        elif request.POST['size'] == 'large':
            print "Your animal is large sized"

    if not 'color' in request.POST:
        print "no color chosen"
        animal['color'] = 'black'
    else:
        animal['color'] = request.POST['color']
        print ("you chose " + request.POST['color'])

    if not 'fly' in request.POST:
        print 'Your animal cannot fly'
    else:
        print 'Your animal can fly!'
        animal['fly'] = 'can'

    if not 'walk' in request.POST:
        print 'Your animal cannot walk'
    else:
        print 'Your animal can walk!'
        animal['walk'] = 'can'
    
    if not 'swim' in request.POST:
        print 'Your animal cannot swim'
    else:
        print 'Your animal can swim!'
        animal['swim'] = 'can'


    print "*"*50
    print "Your animal in object form: "
    print animal
    print "Your animal_list in session is: "

    if not 'animal_list' in request.session:
        request.session['animal_list'] = []
        request.session['animal_list'].append(animal)
    else:
        animal_list = request.session['animal_list']
        animal_list.append(animal)
        request.session['animal_list'] = animal_list
    print request.session['animal_list']
    for x in request.session['animal_list']:
        print "*"*40
        print x['species']
        print "*"*40


    return  redirect("/session_words/animal")
    
def odell(request):
    return HttpResponse("odell catches everything")