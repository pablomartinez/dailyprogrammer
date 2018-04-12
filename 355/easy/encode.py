ENCODING_PAD = dict()


def encrypt(key, msg):
    pad = key * ((len(msg) // len(key)) + 1)
    encoded = ''
    for i, c in enumerate(msg):
        encoded += ENCODING_PAD[pad[i]][ord(c) - ord('a')]
    return encoded


def decrypt(key, msg):
    pad = key * ((len(msg) // len(key)) + 1)
    decoded = ''
    for i, c in enumerate(msg):
        n = ENCODING_PAD[pad[i]].find(c)
        decoded += chr(ord('a') + n)
    return decoded


s = ''.join([chr(c) for c in range(ord('a'), ord('z') + 1)])
n = 0
for c in range(ord('a'), ord('z') + 1):
    ENCODING_PAD[chr(c)] = s[n:] + s[:n]
    n += 1
