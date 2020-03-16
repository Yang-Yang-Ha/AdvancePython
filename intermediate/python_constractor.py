import sys_logging


class Demo:
    # __new__ is a static class method that lets us control object creation.
    # Whenever we make a call to the class constructor, it makes a call to __new__.
    # While this is a default function for every class, we can definitely play around with it.
    # def __new__(cls, *args, **kwargs):
    #     return cls

    def __init__(self):
        self.detoxifying = True

    def show(self):
        sys_logging.info('I detoxify') if self.detoxifying else sys_logging.info('I do not detoxify')


d = Demo()
d.newAttributes = 'new attributes'
sys_logging.info(d.newAttributes)
d.show()
