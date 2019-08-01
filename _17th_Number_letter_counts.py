# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Number letter counts

Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""

"""
1 one   3
2 two   3
3 three 5
4 four  4
5 five  4
6 six   3
7 seven 5
8 eight 5
9 nine  4
10 ten  3
11 eleven   6
12 twelve   6
13 thirteen 8
14 fourteen 8
15 fifteen  7
16 sixteen  7
17 seventeen    9
18 eighteen 8
19 nineteen 8
20 twenty 6
21 twenty-one   9
22 twenty-two   9
23 twenty-three 11
24 twenty-four  10
25 twenty-five  10
26 twenty-six   9
27 twenty-seven 11
28 twenty-eight 11
29 twenty-nine  10
30 thirty 6
40 forty  5
50 fifty  5
60 sixty  5
70 seventy 7
80 eighty 6
90 ninety 6
"""

int2letter = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5,
              8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8,
              15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30:6,
              40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 100:10, 1000:11}

def countUnder20(m):
    return int2letter[m]

def countUnder100(m):
    remainder = m % 10
    if remainder == 0:
        return int2letter[m]
    else:
        return int2letter[m-remainder] + int2letter[remainder]

def countUnder1000(m):
    if m == 1000:
        return int2letter[m]
    remainder = m % 100
    if remainder == 0:
        return int2letter[m//100] + len('hundred')
    elif remainder <= 20:
        return int2letter[m // 100] + len('hundred') + len('and') + countUnder20(remainder)
    else:
        return int2letter[m//100] + len('hundred') + len('and') + countUnder100(remainder)


allCounts = 0
for i in range(1, 1001):
    print(i, allCounts)
    if i <= 20:
        allCounts += countUnder20(i)
    elif i < 100:
        allCounts += countUnder100(i)
    else:
        allCounts += countUnder1000(i)
logging.debug(allCounts)