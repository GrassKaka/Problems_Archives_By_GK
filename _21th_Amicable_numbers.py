# -*- coding: utf-8 -*-
import logging
from functools import reduce

import numpy as np

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Amicable numbers

Problem 21
Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair 
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 
44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

# 列出一个数字的因数
def listDivisors(number):
    divisorsList = [1]
    for i in range(2, int(np.sqrt(number)) + 1):
        if number % i == 0 and number / i == i:
            divisorsList.append(i)
        elif number % i == 0:
            divisorsList.append(i)
            divisorsList.append(number // i)
    return reduce(lambda x, y: x + y, divisorsList)


amicableList = []

for number in range(2, 10000):
    if number in amicableList:
        continue
    sum1 = listDivisors(number)
    sum2 = listDivisors(sum1)
    if sum2 == number and number != sum1:
        amicableList.append(number)
        amicableList.append(sum1)

logging.debug(sum(amicableList))