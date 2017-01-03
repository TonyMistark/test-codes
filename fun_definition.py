#!/usr/bin/env python
# encoding: utf-8

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "<b/>"
    return wrapped

def makitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makitalic
def hello():
    return "hello world"

if __name__  == "__main__":
    print hello()
