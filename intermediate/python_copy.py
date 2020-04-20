import copy

import sys_logging


def deep_copy():
    sys_logging.info(f'------ deep copy ------')
    a = [1, 23, [4, 5], 'Stephen']
    sys_logging.info(f'a = {a}, id(a) = {id(a)}')
    b = copy.deepcopy(a)
    sys_logging.info(f'b = {b}, id(b) = {id(b)}')
    b[2][0] = 23
    b[3] = 'Young'
    sys_logging.info(f'a = {a}, b = {b}, id(a) = {id(a)}, id(b) = {id(b)}')


def shallow_copy():
    sys_logging.info(f'------- shallow copy ------')
    a = [1, 23, [4, 5], 'Stephen']
    sys_logging.info(f'a = {a}, id(a) = {id(a)}')
    b = copy.copy(a)
    sys_logging.info(f'b = {b}, id(b) = {id(b)}')
    b[2][0] = 45
    b[3] = 'Young'
    sys_logging.info(f'a = {a}, b = {b}, id(a) = {id(a)}, id(b) = {id(b)}')


if __name__ == '__main__':
    deep_copy()
    shallow_copy()
