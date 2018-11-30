#!/usr/bin/env python
# encoding: utf-8
import datetime
import functools


def log(func):
    def wrapper(*args, **kwargs):
        print("log: call %s():" % func.__name__)
        return func(*args, **kwargs)
    return wrapper


def log2(func):
    def wrapper(*args, **kwargs):
        print("log2: ---log2---")
        return func(*args, **kwargs)
    return wrapper


def log3(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("log3: %s %s():" % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


def log4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("log4: %s %s()" % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log
@log2
@log3("execute")
@log4("execute")
def now():
    print(datetime.datetime.now())


if __name__ == "__main__":
    now()
