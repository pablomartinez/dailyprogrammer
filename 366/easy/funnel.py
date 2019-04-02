#!/usr/bin/env

def funnel(a, b):
    if len(a) == len(b) + 1:
        for n in range(0,len(a)):
            new = a[:n] + a[n+1:]
            print(new, b) 
            if new == b:
                return True
    return False

def numerical_increment(n):
    remain = n
    pos = 0
    result = 0
    while remain:
        d = remain % 10
        remain = remain // 10
        result += (d+1)*(10**pos)
        if d==9:
            pos += 2
        else:
            pos +=1
    return result
