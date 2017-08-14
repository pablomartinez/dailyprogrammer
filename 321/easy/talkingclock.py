#!/usr/bin/env python
"""
This is the "Talking Clock" dailyprogrammer easy challenge.

https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/

>>> talking_clock('00:00')
"It's twelve am"
"""

def talking_clock(time):
    """ Returns a string representing the time

    Args:
        time (str): A time in 24h format, with the HH:MM format

    Returns:
        str: A representation in natural language of the time
            in 12h (am/pm) notation.

    Test cases 

    >>> talking_clock("00:00")
    "It's twelve am"

    >>> talking_clock("01:30")
    "It's one thirty am"

    >>> talking_clock("12:05")
    "It's twelve oh five pm"

    >>> talking_clock("14:01")
    "It's two oh one pm"
    
    >>> talking_clock("20:29")
    "It's eight twenty nine pm"
    
    >>> talking_clock("21:00")
    "It's nine pm"
    """
    hh, mm = time.split(":")
    h = int(hh)
    m = int(mm)
    numbers = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty")
    decimals = ("twenty", "thirty", "forty", "fifty")
    ampm = "am"
    if h>=12:
        ampm = "pm"
    h = h % 12
    if h == 0:
        h = 12
    hh = numbers[h-1]
    mm = ""
    if m > 0:
        d1 = m % 10
        d2 = m / 10
        if m < 10:
            mm = "oh " + numbers[d1-1]
        elif m < 20:
            mm = decimals[d1-1]
        else:
            mm = decimals[d2-2]
            if d1 > 0:
                mm += " " + numbers[d1-1]
    if mm:
        mm = " " + mm
    return "It's {}{} {}".format(hh, mm, ampm)
