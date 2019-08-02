# -*- coding: utf-8 -*-
import logging
from functools import reduce

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Names scores

Problem 22
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, 
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

with open('_22th_Names_scores.txt', 'r') as f:
    nameContents = f.read()
    nameList = nameContents.replace('"', '').split(',')

# logging.debug(sorted(nameList).index('COLIN'))


def name2score(name):
    return sum(map(ord, name)) - 64 * len(name)

# logging.debug(name2score('COLIN'))

allScores = 0
for index, name in enumerate(sorted(nameList)):
    # print(index, name)
    nameScore = reduce(lambda x, y: x + y, map(name2score, name)) * (index + 1)
    allScores += nameScore

logging.debug(allScores)