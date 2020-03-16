import sys_logging


class MyError(Exception):
    pass


try:
    for i in range(3):
        sys_logging.info(3 / i)
except (ZeroDivisionError, TypeError):
    sys_logging.error('invalid input')
finally:
    sys_logging.info('This will print no matter what')
b = 1

if b == 0:
    raise ValueError('inappropriate value')

try:
    sys_logging.info(1)
    assert 2 + 2 == 4, 'this is wrong'
    sys_logging.info(2)
    assert 1 + 2 == 4, 'this is wrong'
    print(3)
except:
    sys_logging.info('An assert failed')
finally:
    sys_logging.info('Okay')

sys_logging.info('Bye')
