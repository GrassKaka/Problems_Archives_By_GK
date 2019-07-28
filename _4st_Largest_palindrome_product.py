# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Largest palindrome product

Problem 4

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# 判断数字是否是回文数
def isPalindrome(number):
    if str(number) == str(number)[::-1]:
        return True

allProducts = []

for i in range(100, 999):
    for j in range(100, 999):
        allProducts.append(i*j) # 得到两个三位数相乘得到的数字列表

logging.debug(max(filter(isPalindrome, allProducts))) # filter函数过滤，取最大值

