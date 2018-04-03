#!/usr/bin/env python
import sys


def get_3sum(number_list):
    numbers = sorted(list(number_list))
    results = set()
    for x, a in enumerate(numbers[:-2]):
        for y, b in enumerate(numbers[(x + 1):-1]):
            for z, c in enumerate(numbers[(x + y + 2):]):
                if a + b + c == 0:
                    results.add(tuple(sorted([a, b, c])))
    return (results)


if __name__ == '__main__':
    while True:
        num = input().split()
        result = get_3sum([int(n) for n in num])
        print(result)
