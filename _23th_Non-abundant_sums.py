# -*- coding: utf-8 -*-
import logging
from functools import reduce
import numpy as np

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Non-abundant sums

Problem 23
A perfect number is a number for which the sum of its proper divisors 
is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is 
less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be 
written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though 
it is known that the greatest number that cannot be expressed as the sum of 
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be 
written as the sum of two abundant numbers.
"""


# 列出一个数字的因数
def sumDivisors(number):
    divisorsList = [1]
    for i in range(2, int(np.sqrt(number)) + 1):
        if number % i == 0 and number / i == i:
            divisorsList.append(i)
        elif number % i == 0:
            divisorsList.append(i)
            divisorsList.append(number // i)
    return reduce(lambda x, y: x + y, divisorsList)


# 判断数字是不是aboundant number(it is called abundant if this sum exceeds n)
def isabundant(number):
    if sumDivisors(number) > number:
        return True
    else:
        return False


abundantList ,no2abundantList, yes2abundantList = [], [], []
maxint = 28123
t_list = [0] * (maxint)  # 要遍历的数据

for number in range(1, maxint + 1):
    t_index = number - 1
    # 1表示该数过剩，2表示该数可被两个过剩数相加
    if isabundant(number):
        if t_list[t_index] != 2:
            t_list[t_index] = 1  # 第一次被判断为abundant，记为1
        abundantList.append(number)
        for value in abundantList:
            if number + value <= maxint:
                t_list[t_index + value] = 2  #

sumno2abundantList = 0
for index, item in enumerate(t_list):
    if item != 2:
        sumno2abundantList += (index + 1)

logging.debug(sumno2abundantList)
