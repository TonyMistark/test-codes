#!/usr/bin/env python
# encoding: utf-8
import datetime
import functools
import threading


def monitor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        rsp = func(*args, **kwargs)
        end = datetime.datetime.now()
        usedmsec = (end - start).seconds * 1000 + (end - start).microseconds / 1000.0
        print("%s: start-end:[%s~%s], used: %0.2f ms" %(func.__name__, start, end, usedmsec))
        return rsp
    return wrapper


def x(n):
    while n > 0:
        n -= 1

@monitor
def decrement(n):
    x(n)

class MultTread(object):

    @monitor
    def start(self):
        t1 = threading.Thread(target=x, args=[50000000])
        t2 = threading.Thread(target=x, args=[50000000])
        t1.start()
        t2.start()
        t1.join()
        t2.join()

if "__main__" == __name__:
    decrement(100000000)
    MultTread().start()
