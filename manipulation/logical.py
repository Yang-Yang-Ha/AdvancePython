import sys_logging

a = 7 > 7 and 2 > -1
sys_logging.info("and: 7 > 7 and 2 > -1 - " + str(a))

b = 7 > 7 or 2 > -1
sys_logging.info("or: 7 > 7 or 2 > -1 - " + str(b))

c = not 2 > -1
sys_logging.info("not: not 2 > -1 - " + str(c))

d = 7 and 0 or 5
sys_logging.info("7 and 0 or 5 - " + str(d))
