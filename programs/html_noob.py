__author__ = 'blazer1461'
from flask import Flask, render_template
from utils import ExampleModule as reader
from random import choice
html_noob= Flask(__name__)

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

@html_noob.route("/markov")
@html_noob.route("/markov/")
def both_text_files():
   return render_template("combination.html", combination= different_text('utils/data/combination.txt'), title= "Combination Code", header="Markov Combination Code")

@html_noob.route("/markov/sawyer")
def sawyer():
    return render_template("sawyer.html", sawyer= different_text('utils/data/sawyer.txt'), title= "Sawyer Code", header= "Markov Sawyer Code" )


@html_noob.route("/markov/sherlock")
def sherlock():
    return render_template("sherlock.html", sherlock= different_text('utils/data/sherlock_text.txt'), title= "Sherlock Code", header= "Markov Sherlock Code")

@html_noob.route("/markov/war")
def war_of_the_worlds():
    return render_template("war.html", war= different_text('utils/data/war_of_the_worlds_clean.txt'), title= "War of the Worlds Code", header= "Markov War of the Worlds Code")

if __name__ == '__main__':
    html_noob.debug = True
    html_noob.run(host= '0.0.0.0', port= 12345)