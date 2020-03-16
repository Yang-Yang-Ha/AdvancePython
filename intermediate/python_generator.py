from itertools import count

import sys_logging


def generator():
    for i in count():
        yield i


s = generator()
sys_logging.info(next(s))
sys_logging.info(next(s))
