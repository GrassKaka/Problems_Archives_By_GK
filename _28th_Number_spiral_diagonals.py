# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

count = 1

for number in range(3, 1002, 2):
    end_number = number**2
    # print(number, 'end_number', end_number)

    isochromatic_diff = (end_number - (number-2)**2)//4

    start_number = end_number - isochromatic_diff * 3

    # print(number, 'start_number', start_number)
    count += 2 * (end_number + start_number)

logging.debug(count)