import sys_logging

a, b = 3, 2
sys_logging.info(f'before swap, a and b = {a, b} ')
a, b = b, a
sys_logging.info(f'after swap, a and b = {a, b} ')
