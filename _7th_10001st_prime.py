# -*- coding: utf-8 -*-
import logging
import numpy as np

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
10001st prime

Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?
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


n = 1
countPrime = 0
while countPrime < 10001:
    n += 1
    if isPrime(n):
        countPrime += 1

logging.debug(n)