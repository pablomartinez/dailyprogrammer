#!/usr/bin/env
import os

def funnel(a, b):
    if len(a) == len(b) + 1:
        for n in range(0,len(a)):
            new = a[:n] + a[n+1:]
            if new == b:
                return True
    return False

def load_words():
    filename = os.path.join ( os.path.dirname(os.path.realpath(__file__)), 'enable1.txt')
    with open(filename) as f:
        words = [ w.strip() for w in f.readlines()]
    return words

def bonus(word, words):
    similar = []
    for w in words:
        if funnel(word, w):
            similar.append(w)
    return similar
