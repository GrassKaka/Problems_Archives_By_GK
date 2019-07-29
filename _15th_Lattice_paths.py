# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Lattice paths

Problem 15
Starting in the top left corner of a 2×2 grid, 
and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

# def cal_next_lst(now_lst):
#     next_lst = []
#     for index in range(0, len(now_lst)):
#         mid_sum = sum(now_lst[:index+1])
#         next_lst.append(mid_sum)
#     next_lst.append(2*sum(now_lst))
#     return next_lst
#
#
# def cal_counts(n):
#     if n == 1:
#         return [1]
#     else:
#         count_lst = [1]
#         for i in range(1, n):
#             count_lst = cal_next_lst(count_lst)
#         return count_lst
#
# lst = cal_counts(20)
# print(20, 2*sum(lst))


dict = {}


def calcFunc(i, j):
    rest = dict.get(str(i) + ',' + str(j))
    if rest != None:
        return rest
    else:
        if i == 0 or j == 0:
            return 1
        temp = calcFunc(i - 1, j) + calcFunc(i, j - 1)
        dict[str(i) + ',' + str(j)] = temp
        return temp


countSteps = calcFunc(20, 20)

logging.debug(countSteps)