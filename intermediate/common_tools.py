import dis
import pdb
import tabnanny
from random import shuffle
import sys_logging


def add():
    a = 3
    b = 4
    pdb.set_trace()
    c = a + b
    sys_logging.info(f'{a} + {b} + {c}')


def randomize_list_in_place():
    list_a = [1, 2, 3, 4, 5, 6]
    shuffle(list_a)
    sys_logging.info(f'list_a = {list_a}, after randomizing, list_a = {list_a}')


def remove_white_space_in_string():
    a = ' Stephen '
    sys_logging.info(f'a = |{a}|, a.lstrip() = |{a.lstrip()}|')
    sys_logging.info(f'a = |{a}|, a.rstrip() = |{a.rstrip()}|')
    sys_logging.info(f'a = |{a}|, a.strip() = |{a.strip()}|')


if __name__ == '__main__':
    add()
    # To convert bytecode into a more human-readable format, Python has the ‘dis’ module.
    # You can say that it compiles a script, disassembles the bytecode, and prints the output to the STDOUT.
    # dis.dis(add)
    sys_logging.info(tabnanny.check('decorator.py'))
    randomize_list_in_place()
    remove_white_space_in_string()
    x = (lambda a, b: a if a > b else b)(3, 3.5)
    sys_logging.info(x)
