import sys_logging


class Mother:
    id = 'mother'


class Father:
    id = 'father'


class Child(Mother, Father):
    pass


sys_logging.info(issubclass(Child, Mother) and issubclass(Child, Father))
sys_logging.info(Child.mro())
sys_logging.info(Child.id)
