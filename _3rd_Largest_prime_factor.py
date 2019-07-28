# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# 创建获取被除数最大素因数（除了本身）的函数
def maxFactor(divided_number):
    start_factor = 2  # 开始测试的除数
    lastFactor = 1  #
    while divided_number > 1: # 如果被除数大于1，则说明还没找到最大素因数
        if divided_number % start_factor == 0:  # 判断被除数是否能除尽测试的除数
            lastFactor = start_factor # 能够除尽，更新最大的素因数
            divided_number = divided_number / start_factor
            while divided_number % start_factor == 0:
                divided_number = divided_number / start_factor
        start_factor = start_factor + 1 # 将一个测试除数完全除尽，被测试除数加1继续除
    return lastFactor

logging.debug(maxFactor(600851475143)) # 开始计算
