# -*- coding: utf-8 -*-
import logging
from functools import reduce
import numpy as np

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Smallest multiple

Problem 5
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20?
"""

# logging.debug(2*3*2*5*7*2*3*11*13*2*17*19)

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

# 将列表中的所有数相乘
def multiAll(multiLst):
    return reduce(lambda x, y: x *y, multiLst)


allFactors = [] # 搜集最小因数

for number in range(2, 21):
    if isPrime(number):
        allFactors.append(number) # 质数均是其自身的最小因数
    else:
        allProducts = [] # 搜集合数在最小因数列表中的数字
        for factor in allFactors:
            if number % factor == 0:
                allProducts.append(factor)
        if multiAll(allProducts) % number == 0: # 如果搜集的因数相乘是测试数字的整数倍，则继续下一个
            continue
        else: # 否则，需要为这个数字添加一个最小因数到最小因数列表
            allFactors.append(int(number / multiAll(allProducts)))

logging.debug(multiAll(allFactors))


