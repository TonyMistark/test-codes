#!/usr/bin/env python
# encoding: utf-8


class TestIter(object):
    def __init__(self):
        self.lst = [1, 2, 3, 4, 5, 6, 8, 7]

    def read(self):
        for i in range(len(self.lst)):
            yield i

    def __iter__(self):
        return self.read()

    def __str__(self):
        return ",".join(map(str, self.lst))

    __repr__ = __str__


def test_iter():
    obj = TestIter()
    for num in obj:
        print("num", num)
    print("obj", obj)


if __name__ == "__main__":
    test_iter()
