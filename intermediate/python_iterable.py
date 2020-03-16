import dis
from itertools import count, cycle, repeat

import sys_logging

dis.dis('for i in [1, 2, 3]: pass')

nums = [1, 2, 3]
numbers = iter(nums)
next(numbers)
next(numbers)
next(numbers)
sys_logging.info(type(numbers))

a = iter([1, 2, 3])
b = iter(a)
sys_logging.info(a)
sys_logging.info(b)
sys_logging.info(next(a))
sys_logging.info(next(b))
sys_logging.info(next(a))

# count()
for i in count(7, 2):
    if i > 14:
        break
    sys_logging.info(i)

# cycle()
c = 0
for i in cycle(['red', 'blue']):
    if c > 7:
        break
    sys_logging.info(i)
    c += 1

# repeat
c = 0
for i in repeat(['red', 'blue']):
    if c > 7:
        break
    sys_logging.info(i)
    c += 1
