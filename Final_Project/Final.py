__author__ = 'blazer1461'

from random import random
from flask import Flask, render_template
from utils import ExampleModule as reader
from random import choice
final= Flask(__name__)

def generate_chains( fname ):
    chains = {}
    text = reader.read_file( fname )

    words = text.split()
    i = 0
    while i < len(words) - 2:
        key = words[i] + ' ' + words[i+1]
        value = words[i+2]
        if key in chains:
            chains[ key ].append( value )
        else:
            new_list = []
            new_list.append( value )
            chains[ key ] = new_list
        i+= 1
    #print chains
    return chains


def generate_text( chains, num_words ):
    key = choice( chains.keys() )
    s = key
    i = 0
    while i < num_words:
        word = choice( chains[ key ] )
        s+= ' ' + word
        key = key.split()[-1] + ' ' + word
        i+= 1
    return s

def different_text(text_name):
    chains= generate_chains(text_name)
    text= generate_text(chains, 500)


    return text

# rot13



def encryptString (theString):
    rotation = 13 # %=26
    encrypted = ""
    length = len(theString)
    for ex in xrange(length):
        tempStr = theString[ex]
        #print tempStr
        tempInt = ord(tempStr)
        #print tempInt
        if (tempInt >= 65 and tempInt <= 90) or (tempInt >= 97 and tempInt <= 122):#check if letter
            temp = tempInt + rotation
            #print temp
            if (temp >= 97 and temp <= 122) or (temp >= 65 and temp <= 90):#check is rotation does not need help
                encrypted += chr(temp)
            elif temp > 122:
                 encrypted += chr(temp - 26)
            elif temp > 90 and temp < 110:
                encrypted += chr(temp - 26)
            else:
                encrypted += chr(temp)
        else:
            encrypted += tempStr
    return encrypted

def decryptString (theString): #or (theString, key)
    return encryptString (theString)


#Sengen


words = reader.get_csv_dict( 'utils/data/wordlist.csv' )
nouns = words['nouns']
verbs = words['verbs']
adjs = words['adjectives']
advbs = words['adverbs']
articles = ['a','an','the','one']

#takes list of words, returns 1 randomly chosen word
def one_of( g ):
    return g[ int( random() * len(g) ) ]


#wrapper functions for readability
def noun():
    return one_of( nouns )
def verb():
    return one_of( verbs )
def adjective():
    return one_of( adjs )
def article():
    return one_of( articles )
def adverb():
    return one_of( advbs )


def adjectives():
    if random() < .4:
        return ''
    else:
        return adjective() + ' ' + adjectives()


def adverbs():
    if random() < .4:
        return ''
    else:
        return adverb() + ' ' + adverbs();


def article_toggle():
    if random() < .4:
        return article() + ' '
    else:
        return ''


def noun_phrase():
    return article_toggle() + adjectives() + noun() + ' '


def noun_phrase_toggle():
    if random() < .4:
        return noun_phrase() + ' '
    else:
        return ''


def verb_phrase():
    return adverbs() + verb() + ' ' + noun_phrase_toggle()



@final.route("/sengen")
def sengen():
    return render_template("sengen.html", sent_generator="selected", header= "Sentence Generator", title= "Sentence Generator", sengen_file= noun_phrase() + verb_phrase())


@final.route("/main")
@final.route("/")
def main_page():
    return render_template("main_page_syntax.html", header= "Main Page", main_page= "selected", title= "Main Page")


@final.route("/encrypt")
def encrypt():
    return "Ecrypting message"+ render_template("base.html", encrypt_select= "selected")

@final.route("/markov/")
def both_text_files():
    return render_template("book.html", text_generator= "selected", all="selected", the_text= different_text('utils/data/combination.txt'), title= "Combination Code", header="Markov Combination Code")

@final.route("/markov/<book>")
def book(book):
    if book == "sawyer":
        return render_template("book.html", text_generator= "selected", sawyer="selected", the_text= different_text('utils/data/sawyer.txt'), title= "Sawyer Code", header= "Markov Sawyer Code" )

    if book == "sherlock":
        return render_template("book.html", text_generator= "selected", sherlock= "selected", the_text= different_text('utils/data/sherlock_text.txt'), title= "Sherlock Code", header= "Markov Sherlock Code")

    if book == "war":
        return render_template("book.html", text_generator= "selected", war= "selected", the_text= different_text('utils/data/war_of_the_worlds_clean.txt'), title= "War of the Worlds Code", header= "Markov War of the Worlds Code")

if __name__ == '__main__':
    final.debug = True
    final.run(host= '0.0.0.0', port= 12345)