#!/usr/bin/env

def funnel(a, b):
    if len(a) == len(b) + 1:
        for n in range(0,len(a)):
            new = a[:n] + a[n+1:]
            if new == b:
                return True
    return False

def load_words():
    with open('enable1.txt') as f:
        words = [ w.strip() for w in f.readlines()]
    return words

def bonus(word, words):
    similar = []
    for w in words:
        if funnel(word, w):
            similar.append(w)
    return similar
