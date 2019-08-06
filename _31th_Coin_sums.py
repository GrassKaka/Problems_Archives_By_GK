# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Coin sums

Problem 31
In England the currency is made up of pound, £, and pence, p, 
and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

# 解析：每次从列表中取出最大的coin值，得到取最大值个数的上限
#      个数叠加，接下来的用较小的数凑。
# 参考：http://www.itkeyword.com/doc/6678309359658967666/python-projecteuler-problem

def calctimes(value, coins_lst):
	if value == 0 or len(coins_lst)==1 :
		return 1
	else:
		sortedcoins_lst = sorted(coins_lst)
		largest = sortedcoins_lst[-1]
		uses = value // largest
		count = 0
		for i in range(uses+1):
			count += calctimes(value-largest*i, sortedcoins_lst[:-1])
		return count

logging.debug(calctimes(200, [1,2,5,10,20,50,100,200]))