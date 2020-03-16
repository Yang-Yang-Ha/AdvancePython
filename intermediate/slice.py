import sys_logging

# To slice a iterable, we use the slicing operator, that is [ ]. To separate the start, stop, and step values, we use the colon ( : ).
originalList = [1, 2, 3, 4, 5]
sys_logging.info(originalList[1:4])

# slice() function
sys_logging.info(originalList[slice(3)])
sys_logging.info('helloworld'[slice(1, 6, 2)])

# negative index
sys_logging.info(originalList[slice(-1, -5, -2)])
sys_logging.info(originalList[-1: -5: -2])
sys_logging.info(originalList[: -1])

sys_logging.info(originalList[:: -1])
sys_logging.info(originalList[1:4])
originalList[1:4] = [6, 7, 8, 9]
sys_logging.info(originalList)
del originalList[1:4]
sys_logging.info(originalList)
