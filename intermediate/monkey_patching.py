import sys_logging


class A:
    @staticmethod
    def func():
        sys_logging.info(f'class A original func')


if __name__ == '__main__':
    def refactor_func():
        sys_logging.info(f'This is refactor func')


    A.func = refactor_func
    A.func()
