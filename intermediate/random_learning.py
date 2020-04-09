import random
import sys_logging


def test_seed():
    for i in range(2):
        random.seed(2)
        for j in range(20):
            sys_logging.info(f'{i} + {random.random()}')


def test_shuffle():
    my_list = ['apple', 'berry', 'cherry']
    random.seed(2)
    for i in range(2):
        random.shuffle(my_list)
        print(my_list)


if __name__ == '__main__':
    # test_seed()
    test_shuffle()
