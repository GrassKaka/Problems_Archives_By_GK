# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')
"""
Number spiral diagonals

Problem 28
Starting with the number 1 and moving to the right in a clockwise direction 
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?
"""

count = 1

for number in range(3, 1002, 2):
    end_number = number**2
    # print(number, 'end_number', end_number)

    isochromatic_diff = (end_number - (number-2)**2)//4

    start_number = end_number - isochromatic_diff * 3

    # print(number, 'start_number', start_number)
    count += 2 * (end_number + start_number)

logging.debug(count)