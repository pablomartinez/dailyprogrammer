#!/usr/bin/env
import random

def throw_dices(dices):
    """ Returns the result of throwing one or more dices 

    This function expects a string in the format `{n}d{m}` where `n`
    is the number of dices and `m` the type of dice. So the string
    "3d6" means 3 dices with 6 sides each.

    Args:
        dices (str): The number of dices in D&D format

    Returns:
        int: A random number simulating throwing the dices.
    """
    result = 0
    n, m = dices.split('d')
    for i in range(int(n)):
        result += random.randint(1,int(m))
    return result

