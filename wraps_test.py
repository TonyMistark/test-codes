#!/usr/bin/env python
# encoding: utf-8

from functools import wraps


def my_decorator(func):
    #@wraps(func)
    def wrapper(*args, **kwds):
        print "Calling decorated function"
        return func(*args, **kwds)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print "Called example function"


if __name__ == "__main__":
    example()
    print example.__name__
    print example.__doc__
