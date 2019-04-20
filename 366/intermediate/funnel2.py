#!/usr/bin/env
import os

def find_longest_funnel(word, words):
    chains = find_chains(word,words)
    funnel_chains = []
    for chain in chains:
        funnel_chains.append([word] + chain)
    
    return max([len(c) for c in funnel_chains]) if funnel_chains else 1

def find_chains(word, words):
    """ Returns the chains of funnels

    Args: 
        word (str): The word to find the funnels
        words (list): The list of words to search in

    Returns:
        list: A list of chains. Each chain is a list of nested  words,
            not including the original one.
    """
    chains = []
    if len(word) > 1:
        funnels = find_funnels(word, words)
        for funnel in funnels:
            new_chains = find_chains(funnel, words)
            if new_chains:
                for chain in new_chains:
                    chains.append([funnel] + chain)
            else:
                chains.append([funnel])
    return chains
        
def find_funnels(word, words):
    """ Returns all the funnels for word.

    Args: 
        word (str): The word to find the funnels
        words (list): The list of words to search in
    
    Returns:
        list: The list of words that are funnel from the  `word`
    """
    funnels = []
    for w in words:
        if len(word) == len(w) + 1:
            for n in range(0,len(word)):
                new = word[:n] + word[n+1:]
                if new == w:
                    funnels.append(w)
    return funnels

def load_words():
    filename = os.path.join ( os.path.dirname(os.path.realpath(__file__)), 'enable1.txt')
    with open(filename) as f:
        words = [ w.strip() for w in f.readlines()]
    return words