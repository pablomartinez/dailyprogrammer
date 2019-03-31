#!/usr/bin/env

def increment(n):
    result = ''
    for d in str(n):
        result += str(int(d)+1)
    return int(result)

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