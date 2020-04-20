from itertools import count
from typing import Generator, Iterable, Iterator
import sys_logging


def create_generator():
    for i in count():
        yield i


def generator_test():
    s = create_generator()
    sys_logging.info(type(s))
    sys_logging.info(issubclass(Iterable, Iterator))
    sys_logging.info(next(s))
    sys_logging.info(next(s))


if __name__ == '__main__':
    generator_test()
