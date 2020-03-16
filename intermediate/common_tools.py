import dis
import tabnanny
import pdb
import sys_logging


def add():
    a = 3
    b = 4
    pdb.set_trace()
    c = a + b
    sys_logging.info(f'{a} + {b} + {c}')


add()
# To convert bytecode into a more human-readable format, Python has the ‘dis’ module.
# You can say that it compiles a script, disassembles the bytecode, and prints the output to the STDOUT.
dis.dis(add)

sys_logging.info(tabnanny.check('decorator.py'))
