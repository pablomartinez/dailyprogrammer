from math import sqrt


def get_decomposition_sum(num):
    pairs = []
    upper_limit = int(sqrt(num)) + 1
    for n in range(1, upper_limit):
        if num % n == 0:
            pairs.append((n, num / n))
    p = min(pairs, key=lambda x: x[0] + x[1])
    print("Found ", p)
    return p[0] + p[1]
