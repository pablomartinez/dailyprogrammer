def persistence(n):
    if n <= 9:
        return 0
    else:
        return 1 + persistence(sum([int(d) for d in str(n)]))

def numerical_persistence(n):
    num = n
    count = 0
    while num>9:
        count += 1
        digits = 0
        while num:
            digits += num%10
            num = num//10
        num = digits
    return count
