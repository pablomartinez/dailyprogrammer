ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encode62(num):
    if num == 0:
        return '0'
    result = ''
    remaining = num
    while remaining > 0:
        result = ALPHABET[remaining % 62]+ result
        remaining = int(remaining / 62)
    return result
