def distance(s1, s2):
    d = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            d += 1
    return d


def closest(items):
    distances = list()
    for item in items:
        distances.append([item, sum([distance(item, i) for i in items])])
    c = min(distances, key=lambda d: d[1])
    return c[0]
