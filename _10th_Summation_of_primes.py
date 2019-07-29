# -*- coding: utf-8 -*-
import logging
import numpy as np

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Summation of primes

Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

# 判断一个数是否为质数
def isPrime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, int(np.sqrt(number))+2):
        if number % i == 0:
            return False
    return True

n=1
sumPrime = 0
while n < 2000000:
    n += 1
    if isPrime(n):
        sumPrime += n

logging.debug(sumPrime)
