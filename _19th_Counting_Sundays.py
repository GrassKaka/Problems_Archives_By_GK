# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')

"""
Counting Sundays

Problem 19
You are given the following information,
but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, 
but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month 
during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


noleapList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapList = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapyear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        if year % 4 == 0:
            return True
        else:
            return False


k = 1 # 1901年1月1号是星期二
allSundays = 0

for year in range(1901, 2001):
    if isLeapyear(year):
        for month in leapList:
            for day in range(month):
                k += 1
                if k == 7:
                    if day == 0:
                        # print('Year' + str(year) + '---' + 'Day ' + str(day + 1) + ': ', k)
                        allSundays += 1
                    k = 0
    else:
        for month in noleapList:
            for day in range(month):
                k += 1
                if k == 7:
                    if day == 0:
                        # print('Year' + str(year) + '---' + 'Day ' + str(day + 1) + ': ', k)
                        allSundays += 1
                    k = 0

logging.debug(allSundays)
