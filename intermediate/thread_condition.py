import threading
import time
from threading import Thread

import sys_logging


class SomeItem:
    def __init__(self):
        self.list = []

    def produce(self, item):
        self.list.append(item)

    def consume(self):
        item = self.list[0]
        self.list.remove(item)


def producer(si, cond):
    for i in range(1, 5):
        sys_logging.info(f'Producer acquiring lock')
        cond.acquire()
        sys_logging.info(f'Producer got the lock')
        try:
            time.sleep(i)
            si.produce(i)
            cond.notifyAll()

        finally:
            cond.release()
            sys_logging.info(f'Producer release')


def consumer(si, cond):
    sys_logging.info(f'Consumer acquire lock')
    cond.acquire()
    sys_logging.info(f'Consumer got the lock')
    try:
        si.consume()
    except IndexError:
        sys_logging.info(f'Consumer call wait')
        val = cond.wait(10)
        sys_logging.info(f'Consumer wait finished and got the lock, wait = {val}')
        if val:
            sys_logging.info(f'Consumer notification received about item production...')
        else:
            sys_logging.info(f'Consumer waiting timeout...')
    finally:
        cond.release()
        sys_logging.info(f'consumer release')


def condition_task():
    main_cond = threading.Condition()
    main_si = SomeItem()
    c_thread = Thread(name='Consumer-Thread', target=consumer, args=(main_si, main_cond))
    c_thread.start()
    p_thread = Thread(name='Producer-Thread', target=producer, args=(main_si, main_cond,))
    p_thread.start()
    c_thread.join()
    p_thread.join()
    sys_logging.info(f'Main Done')


def barrier_thread(barrier, timeout):
    thread_name = threading.current_thread().getName()
    sys_logging.info(f'{thread_name} is start')
    time.sleep(timeout)
    if thread_name == 'Thread-Three':
        barrier.abort()
        return
    sys_logging.info(f'{thread_name} is ready')
    try:
        barrier.wait()
    except threading.BrokenBarrierError:
        sys_logging.info(f'{thread_name} is excepted')
    finally:
        sys_logging.info(f'{thread_name} is finished')


def barrier_task():
    barrier_one = threading.Barrier(3)
    thread_one = Thread(name='Thread-One', target=barrier_thread, args=(barrier_one, 1,))
    thread_two = Thread(name='Thread-Two', target=barrier_thread, args=(barrier_one, 3,))
    thread_three = Thread(name='Thread-Three', target=barrier_thread, args=(barrier_one, 10))

    thread_one.start()
    thread_two.start()
    thread_three.start()

    thread_one.join()
    thread_two.join()
    thread_three.join()


if __name__ == '__main__':
    # condition_task()
    barrier_task()
    sys_logging.info(f'Main Done')
