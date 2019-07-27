# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

multiples_3or5_lst = []

for number in range(1, 1000):
    if number % 3 == 0 or number % 5 == 0:
        multiples_3or5_lst.append(number)

logging.debug(sum(multiples_3or5_lst))