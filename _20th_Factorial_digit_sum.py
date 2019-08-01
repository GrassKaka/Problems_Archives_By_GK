# -*- coding: utf-8 -*-
import logging
from functools import reduce

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Factorial digit sum

Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""

def char2int(s):
    basic_dict = {'0': 0,
                  '1': 1,
                  '2': 2,
                  '3': 3,
                  '4': 4,
                  '5': 5,
                  '6': 6,
                  '7': 7,
                  '8': 8,
                  '9': 9,
                  }
    return basic_dict[s]


def calcFactorial(number):
    if number == 1:
        return 1
    if number == 2:
        return 2
    else:
        return number * calcFactorial(number-1)

logging.debug(calcFactorial(100))

logging.debug(reduce(lambda x, y: x+y, map(char2int, str(calcFactorial(100)))))