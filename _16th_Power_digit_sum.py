# -*- coding: utf-8 -*-
import logging
from functools import reduce
from operator import mul

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Power digit sum

Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

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


logging.debug(reduce(lambda x, y: x+y, map(char2int, str(2**1000))))
