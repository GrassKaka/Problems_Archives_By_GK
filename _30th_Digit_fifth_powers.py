# -*- coding: utf-8 -*-
import logging
from functools import reduce

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Digit fifth powers

Problem 30
Surprisingly there are only three numbers that can be written 
as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of 
fifth powers of their digits.
"""


def power5times(stringn):
    return int(stringn) ** 5

def confirmBoundary():
    boundary = 0
    for n in range(1, 11):
        if (9**5)*n < 10**n:
            boundary = (9**5)*n
            break
    return boundary + 1


circleBoundary = confirmBoundary()
n = 2
fifthPowerlist = []

while n < circleBoundary:
    if reduce(lambda x,y:x+y, map(power5times, str(n))) == n:
        fifthPowerlist.append(n)
    n += 1

logging.debug(fifthPowerlist)
logging.debug(sum(fifthPowerlist))

