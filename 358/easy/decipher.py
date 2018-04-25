ENCODING_PAD = dict()

ALPHABET = [(' _ ', '| |', '|_|'), ('   ', '  |', '  |'), (' _ ', ' _|', '|_ '), (' _ ', ' _|', ' _|'), ('   ', '|_|', '  |'), (' _ ', '|_ ', ' _|'), (' _ ', '|_ ', '|_|'), (' _ ', '  |', '  |'), (' _ ', '|_|', '|_|'), (' _ ', '|_|', ' _|')]

def in_chunks(i, n=3):
    return [i[x:x+n] for x in range(0,len(i), n)]

def decipher(s):
    rows = s.split("\n")
    splitted = [in_chunks(r) for r in rows]
    chars = zip(*splitted)
    return ''.join([str(ALPHABET.index(c)) for c in chars])
