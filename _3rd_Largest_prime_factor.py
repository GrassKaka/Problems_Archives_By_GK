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
    basic_factor = 2  # 基础因数
    lastFactor = 1  #
    while divided_number > 1:
        if divided_number % basic_factor == 0:  # 判断被除数是否能除尽最新产生的因数
            lastFactor = basic_factor
            logging.debug(lastFactor)
            divided_number = divided_number / basic_factor
            logging.debug(divided_number)
            while divided_number % basic_factor == 0:
                divided_number = divided_number / basic_factor
                logging.debug(divided_number)
        basic_factor = basic_factor + 1
        logging.debug(basic_factor)
    return lastFactor

# logging.debug(maxFactor(600851475143)) # 开始计算

logging.debug(maxFactor(23456)) # 开始计算