def condense_words(w1, w2):
    common = 0
    length = min(len(w1), len(w2))
    for x in range(1, length):
        if w1.endswith(w2[:x]):
            common = x
    if length == 0 or common > 0:
        return "{0}{1}".format(w1, w2[common:])
    else:
        return "{0} {1}".format(w1, w2)


def condense_sentence(s):
    sentence = ''
    words = s.split()
    for w in words:
        sentence = condense_words(sentence, w)
    return sentence
