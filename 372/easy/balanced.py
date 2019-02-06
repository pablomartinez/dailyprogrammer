def balanced(s):
    return s.count('x') == s.count('y')

def perfect_balanced(s):
    number = 0
    count = {}
    for c in s:
        if c not in count:
            number = count[c] = s.count(c)

    return all([n == number for n in count.values()])
