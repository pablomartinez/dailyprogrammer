#!/usr/bin/python

nonprimes = set()

def primes(n):
    global nonprimes
    for i in range(2, n+1):
        if i not in nonprimes:
            nonprimes.update(range(i*2, n, i))
            yield i

def goldbach(number):
    results = []
    for a in primes(number):
        for b in primes(a):
            for c in primes(b):
                if a+b+c == number:
                    results.append((a,b,c))
    return results
