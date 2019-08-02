# -*- coding: utf-8 -*-
import logging
from functools import reduce

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Lexicographic permutations

Problem 24
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of 
the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import itertools

datas = [x for x in range(10)]
data1 = (1, 2, 3)

logging.debug(reduce(lambda x,y:10*x+y, list(itertools.permutations(datas))[10**6-1]))


# # This solution is written in Python 3.7
# n = 10
# combinations = []
# number = int(1e6)
# digits = {x for x in range(n)}
#
#
# def run(my_list, string):
#     global combinations
#     if len(my_list) == 0:
#         combinations.append(string)
#     for char in my_list:
#         run(my_list - {char}, string + str(char))
#     return None
#
# run(digits, '')
# print(combinations[number-1])