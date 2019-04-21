

def calculate(original_tuple):
    new_tuple = []
    for x in range(len(original_tuple)):
        new_tuple.append(abs(original_tuple[x] - original_tuple[(x + 1) % len(original_tuple)]))
    return tuple(new_tuple)


def ducci(t):
    seq = [t]
    new_tuple = t
    while True:
        new_tuple = calculate(new_tuple)
        # If the tuple is all 0 or already exists, end the sequence
        if (not any(new_tuple)) or new_tuple in seq:
            seq.append(new_tuple)
            return seq
        else:
            seq.append(new_tuple)