__author__ = 'blazer1461'
from flask import Flask, render_template
import ExampleModule as reader
from random import choice
updated_noob= Flask(__name__)

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

@updated_noob.route("/markov")
@updated_noob.route("/markov/")

def both_text_files():
    title="<DOCTYPE HTML><head><title>Markov Code</title></head>"
    headers= "<!DOCTYPE HTML><header><h1>Markov Combination Code</h1></header></b>"
    word_count= "<!DOCTYPE HTML><header><h2>500 words</h1></header>"

    return title+ headers+ word_count+ different_text('combination.txt')

@updated_noob.route("/markov/sawyer")
def sawyer():
    title="<DOCTYPE HTML><head><title>Sawyer Code</title></head>"
    headers= "<!DOCTYPE HTML><header><h1>Markov Sawyer Code</h1></header></b>"
    word_count= "<!DOCTYPE HTML><header><h2>500 words</h1></header>"

    return title+ headers+ word_count+ different_text('sawyer.txt')


@updated_noob.route("/markov/sherlock")
def sherlock():
    title="<DOCTYPE HTML><head><title>Sherlock Code</title></head>"
    headers= "<!DOCTYPE HTML><header><h1>Markov Sherlock Code</h1></header></b>"
    word_count= "<!DOCTYPE HTML><header><h2>500 words</h1></header>"

    return title+ headers+ word_count+ different_text('sherlock_text.txt')


if __name__ == '__main__':
    updated_noob.debug = True
    updated_noob.run(host= '0.0.0.0', port= 12345)