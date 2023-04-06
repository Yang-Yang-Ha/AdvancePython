#!/usr/bin/env python3

class ClassInstance:
    inita = 2
    def __init__(self) -> None:
        self.inita = 0

    def seta(self, count) -> None:
        self.count = count

    def print(self) -> None:
        print('self inita: {}'.format(self.inita))


instance = ClassInstance()
print('class inita = {}'.format(id(ClassInstance.inita)))
print('class self.inita = {}'.format(id(instance.inita), instance.print()))
print('class inita = {}'.format(ClassInstance.inita))
print('method return type: {}'.format(type(instance.seta(2))))
print('self.count = {}'.format(instance.count))