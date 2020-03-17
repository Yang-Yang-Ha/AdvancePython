import sys_logging


def decor(fun):
    def wrap():
        sys_logging.info('$$$$$$')
        fun()
        sys_logging.info('$$$$$$')

    return wrap


def say_hello():
    sys_logging.info('Hello')


newFunc = decor(say_hello)
newFunc()


# Python decorator with parameters
def checkZero(func):
    def wrapper(a, b):
        if b == 0:
            sys_logging.error('Can not divide 0')
            return
        return func(a, b)

    return wrapper


@checkZero
def divide(a, b):
    return a / b


divide(3, 0)


def decor1(func):
    def wrap():
        print("$$$$$$$$$$$$$$")
        func()
        print("$$$$$$$$$$$$$$")

    return wrap


def decor2(func):
    def wrap():
        print("##############")
        func()
        print("##############")

    return wrap


@decor2
@decor1
def say_bye():
    sys_logging.info('bye')


say_bye()
