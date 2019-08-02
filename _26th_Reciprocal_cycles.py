# -*- coding: utf-8 -*-
import logging
from functools import reduce

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Reciprocal cycles

Problem 26
A unit fraction contains 1 in the numerator. 
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle 
in its decimal fraction part.
"""

# https://www.cnblogs.com/xianglan/archive/2011/03/23/1992601.html 摘抄
"""
我们知道，如果一个数的质因子全是2和5的话，这个数的倒数是不会无限循环的

如2，4，5，8，10

而一个数把质因子中的2和5除去后，得到一个数，我们称之为“基数”吧

这个数和它的基数的倒数循环的长度是相同的

比如说3和6的倒数的循环长度都是1

而怎么计算一个数的循环长度呢

只需要知道它能被多少长度的9整除就行了

3能被9整除，所以它的循环长度是1

7能被999999整除，商正好是循环体142857，所以它的循环长度是6

我想这一点大家应该很好理解吧

有前面的分析我们可以很容易得到这道题的解法

先求一个数的基数，如果是它本身，则计算它的循环长度

如果不是它自身，那它的循环长度等于基数的循环长度

我们规定1的循环长度是0，这样所以只含2，5为质因子的数的基数都为1，循环长度为0
"""

def updateChangenumber(n):
    return reduce(lambda x,y:10*x+y, [9]*n)

def cancelPrimefactors(number):
    while number % 2 == 0:
        number = number // 2
    while number % 5 == 0:
        number = number // 5
    return number


log_dict = {}

for number in range(1, 1001):
    n = 1
    basicNumber = cancelPrimefactors(number)
    if basicNumber == 1:
        log_dict[number] = 0
        continue
    while updateChangenumber(n) % basicNumber != 0:
        n += 1
    log_dict[number] = len(str(updateChangenumber(n) // basicNumber))


ordered_dict=sorted(log_dict.items(),key=lambda x:x[1],reverse=True)
logging.debug(ordered_dict[0])