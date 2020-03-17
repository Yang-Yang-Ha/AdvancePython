import threading
from random import randint
from threading import Thread
from time import sleep

import sys_logging


def thread_basic_print():
    # This returns the number of alive(currently) Thread objects.
    # This is equal to the length the of the list that enumerate() returns.
    sys_logging.info(f'threading.active_count() = {threading.active_count()}')
    sys_logging.info(f'current thread = {threading.current_thread()}')
    sys_logging.info(f'current thread id = {threading.get_ident()}')
    # This returns a list of all alive(currently) Thread objects.
    # This includes the main thread, daemonic threads, and dummy thread objects created by current_thread().
    # This obviously doesn’t include terminated threads as well as those that haven’t begun yet.
    sys_logging.info(f'thread enumerate = {threading.enumerate()}')
    sys_logging.info(f'main thread = {threading.main_thread()}')


def function_one(arg, name):
    sys_logging.info(f'current thread name = {threading.currentThread()}')
    for i in range(arg):
        sys_logging.info(f'{name} -> {arg}')


def function_two(arg, name):
    sys_logging.info('This is function two')
    function_one(arg, name)


# basic tread
def thread_method():
    thread_one = Thread(target=function_one, args=(10, 'ThreadOne'))
    thread_one.start()
    thread_two = Thread(target=function_two, args=(5, 'thread two'))
    thread_two.start()
    thread_two.join()
    sys_logging.info('print after child threads')


class SharedCounter(object):
    def __init__(self, val=0):
        self.lock = threading.Lock()
        self.counter = val

    def increment(self, name):
        sys_logging.info(f'Waiting for a lock at {name}')
        self.lock.acquire()
        sys_logging.info(f'{name} Acquired a lock, counter value = {self.counter}')
        self.counter += 1
        self.lock.release()
        sys_logging.info(f'{name} Released a lock, counter value = {self.counter}')


def task(shared_counter, name):
    r = randint(10, 20)
    for i in range(r):
        shared_counter.increment(name)
    sys_logging.info(f'task {name} done')


# lock thread
def lock_method():
    s_counter = SharedCounter()
    t1 = threading.Thread(target=task, args=(s_counter, 't1',))
    t1.start()
    t2 = threading.Thread(target=task, args=(s_counter, 't2',))
    t2.start()
    t1.join()
    t2.join()
    sys_logging.info(f'Counter: {s_counter.counter}')


rlock = threading.RLock()


def get_first_line():
    sys_logging.info(f'start first line')
    first_acquire = rlock.acquire()
    sys_logging.info(f'first acquire = {first_acquire}')
    try:
        with open('write.txt', 'a') as writeFile:
            first_line = writeFile.write("this is an append line")
            sys_logging.info(f'first: {first_line}')
        sleep(5)
    finally:
        rlock.release()


def get_second_line():
    sys_logging.info(f'start second line')
    second_acquire = rlock.acquire()
    sys_logging.info(f'second acquire = {second_acquire}')
    try:
        with open('write.txt', 'r') as write:
            second_line = write.readlines()
            sys_logging.info(f'second: {second_line}')
    finally:
        rlock.release()


def rlock_method():
    first = Thread(target=get_first_line)
    second = Thread(target=get_second_line)
    first.start()
    second.start()
    first.join()
    second.join()
    return first, second


def test_lock():
    lock = threading.RLock()
    sys_logging.info(f'first time lock {lock.acquire()}')
    sys_logging.info(f'second time lock {lock.acquire()}')


def event_task(event):
    event_set = event.wait()
    sys_logging.info(f'{threading.current_thread()}')
    if event_set:
        sys_logging.info(f'Event received, releasing thread...')
    else:
        sys_logging.info(f'Time out, moving ahead without event')


def event_object():
    # initialize the event object
    e = threading.Event()

    # starting the thread
    event_threading_one = Thread(name='Event-Blocking-Thread-one', target=event_task, args=(e,))
    event_threading_one.start()

    event_threading_two = Thread(name='Event-Blocking-Thread-two', target=event_task, args=(e,))
    event_threading_two.start()
    sleep(5)
    e.set()


def timer_task():
    sys_logging.info(f'Timer object is getting executed')


def timer_object():
    # timer class is the subclass of Thread
    timer_thread = threading.Timer(5, timer_task)
    timer_thread.start()
    sleep(6)


def condition_object():
    pass


if __name__ == '__main__':
    # thread_basic_print()
    # thread_method()
    # lock_method()
    # test_lock()
    # line_one, line_second = rlock_method()
    # sys_logging.info(f'line one = {line_one} \n line two = {line_second}')
    # event_object()
    # timer_object()
    condition_object()
    sys_logging.info(f'main thread finished')
