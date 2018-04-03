def all_sums(n):
    """ Returns a list with all the sums possible with the digits """
    num = str(n)
    results = [n]
    for x in range(1, len(num)):
        r = int(num[:x]) + int(num[x:])
        results.append(r)
    return sorted(results)


def is_kaprekar(n):
    sums = all_sums(n**2)
    return n in sums


if __name__ == '__main__':
    try:
        input = raw_input
    except NameError:
        pass
    s = input()
    a, b = s.split()
    for x in range(int(a), int(b)):
        if is_kaprekar(x):
            print(x)
