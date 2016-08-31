#!/usr/bin/env python
# encoding: utf-8


class Test(object):
    def __init__(self):
        self.callback_list = []

    def register(self, callback):
        self.callback_list.append(callback)

    def do(self):
        print "do"
        for callback in self.callback_list:
            callback()

def f():
    print "f"

def main():
    t = Test()
    t.register(f)
    t.do()

if __name__ == "__main__":
    main()

