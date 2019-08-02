# -*- coding: utf-8 -*-
import logging
import numpy as np

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Quadratic primes

Problem 27
Euler discovered the remarkable quadratic formula:

n**2+n+41
It turns out that the formula will produce 40 primes 
for the consecutive integer values 0≤n≤390≤n≤39. 
However, when n=40,40**2+40+41=40(40+1)+41=40,40**2+40+41=40(40+1)+41 is divisible by 41,
and certainly when n=41,41**2+41+41=41,41**2+41+41 is clearly divisible by 41.

The incredible formula n**2−79n+1601 was discovered, 
which produces 80 primes for the consecutive values 0≤n≤79. 
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n**2+a*n+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11and |−4|=4
Find the product of the coefficients, aa and bb, for the quadratic expression that produces the maximum number of primes for consecutive values of nn, starting with n=0n=0.
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


def productBlist():
    b_list = []
    for i in range(2, 1001):
        if isPrime(i):
            b_list.append(i)
    return b_list


def calcFormula(number, a, b):
    return int(number**2 + number*(a) + b)


def combineAandB():
    list_AandB = []
    for a in range(-999, 1001, 2):
        for b in productBlist():
            list_AandB.append((a, b))
    return list_AandB


maxcountPrime = 0
maxlist_AandB = []
for a, b in combineAandB():
    n = 0
    while calcFormula(n, a, b) >= 2:
        if isPrime(calcFormula(n, a, b)):
            n += 1
        else:
            if n + 1 > maxcountPrime:
                maxlist_AandB.append((a, b))
                maxcountPrime = n + 1
            break

logging.debug(maxcountPrime)
a, b = maxlist_AandB[-1]
logging.debug(a * b)
