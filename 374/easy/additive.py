def persistence(n):
    if n <= 9:
        return 0
    else:
        return 1 + persistence(sum([int(d) for d in str(n)]))
