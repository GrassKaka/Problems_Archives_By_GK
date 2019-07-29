# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Special Pythagorean triplet

Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
a+b>c, a+b+c=1000,1000-c>c, c<500
a+b+c=1000, 3c>1000, c>333
"""

"""
a+b=1000-c, 2b>1000-c, b>(1000-c)/2
"""

for c in range(333, 500):
    for b in range(int((1000 - c)/2), c):
        a = 1000 - c - b
        if a**2 + b**2 == c**2:
            logging.debug(a*b*c)