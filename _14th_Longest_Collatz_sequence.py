# -*- coding: utf-8 -*-
import logging
from time import time
import json

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - [%(levelname)s] : %(message)s')


def isIndict(number, dict):
    if number in dict:
        return dict[number]

# def countCollatzsequence(number):
#     count = 1
#     if number == 0:
#         return "Number can't be zero"
#     if number == 1:
#         return 1
#     while number != 1:
#         if number % 2 ==0:
#             number = number / 2
#         else:
#             number = 3 * number + 1
#         count += 1
#     return count
#
# logging.debug(countCollatzsequence(6))

def fastcountCollatzsequence(number, dict):
    count = 1
    if number == 0:
        return "Number can't be zero"
    if number == 1:
        return 1
    while number != 1:
        if isIndict(number, dict):
            return dict[number] + count
        else:
            if number % 2 ==0:
                number = number / 2
                if isIndict(number, dict):
                    return count + dict[number]
            else:
                number = 3 * number + 1
                if isIndict(number, dict):
                    return count + dict[number]
        count += 1
    return count


# startTime = time()
#
# try:
#     with open('_14th_DatasForCollatzsequence.txt', 'r') as f:
#         log_dict = json.loads(f.read())
# except FileNotFoundError:
#     log_dict = {}
#     with open('_14th_DatasForCollatzsequence.txt', 'w') as f:
#         f.write(json.dumps(log_dict))
#
# active = 0
# for i in range(1, 1000000):
#     if log_dict.get(str(i)):
#         continue
#     else:
#         active = 1
#         log_dict[i] = fastcountCollatzsequence(i, log_dict)
# if active:
#     with open('_14th_DatasForCollatzsequence.txt', 'w') as f:
#         f.write(json.dumps(log_dict))
#
# ordered_dict=sorted(log_dict.items(),key=lambda x:x[1],reverse=True)
# logging.debug(ordered_dict[0])
#
# endTime = time()
#
# usedTime = endTime - startTime
# logging.debug('Time for one million: ' + str(usedTime))

startTime = time()

log_dict = {}
for i in range(1, 1000000):
    if log_dict.get(str(i)):
        continue
    else:
        log_dict[i] = fastcountCollatzsequence(i, log_dict)

ordered_dict=sorted(log_dict.items(),key=lambda x:x[1],reverse=True)
logging.debug(ordered_dict[0])

endTime = time()

usedTime = endTime - startTime
logging.debug('Time for one million: ' + str(usedTime))


"""
2019-07-29 14:15:46,249 - [DEBUG] : (837799, 525)
2019-07-29 14:15:46,250 - [DEBUG] : Time for one million: 10.834000825881958
"""