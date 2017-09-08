#!/usr/bin/env python
"""
This is the 'Spiral Ascension' daily programmer easy challenge.

https://www.reddit.com/r/dailyprogrammer/comments/6i60lr/20170619_challenge_320_easy_spiral_ascension/
"""
import fileinput

def gen_spiral(number):
    """ Returns a list of list with an ascending spiral

    Args:
        number (int): The width of the box.

    Returns:
        tuple: (list, int)
            list: Returns a list of list, with integers that represents a
            matrix that can be drawn
            int: The max width of the any element in the list.
    """

    def rotate(dy,dx):
        """ Changes the directions by rotating them 90 degrees
        
        Args:
            dy (int): Vertical direction: 1 down, 0, up
            dx (int): Horizontal direction: 1 right, 0, left

        Returns:
            tuple (int, int): A tuple with the new directions.
        """
        if dy==0:
            dy = dx
            dx = 0
        elif dx==0:
            dx = -dy
            dy = 0
        return(dy,dx)

    # Initializes data.
    data = [ [ '' for x in range(number) ] for y in range(number)]
    target = number ** 2
    max_width=len(str(target))
    x = 0
    y = 0
    dx = 1
    dy = 0
    # Populate the spiral by going through all the numbers and "rotating" when
    # a limit is reached.
    for n in range(target):
        data[y][x] = n+1
        if x+dx<0 or x+dx>=number or y+dy<0 or y+dy>=number or data[y+dy][x+dx]:
            dy, dx = rotate(dy, dx)
        x += dx
        y += dy
    return data, max_width

if __name__ == '__main__':
    for line in fileinput.input():
        number = int(line)
        spiral, max_width = gen_spiral(number)
        for row in spiral:
            print(' '.join([ "{0:{w}}".format(c,w=max_width) for c in row ]))
