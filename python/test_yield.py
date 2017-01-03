#!/usr/bin/env python
# encoding: utf-8


# python yield 简单使用

#版本１ 费波那契数列
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, (a + b)
        n += 1


#版本２ 返回列表
def fab2(max):
    n, a, b = 0, 0, 1
    fab_list = []
    while n < max:
        fab_list.append(b)
        a, b = b, (a + b)
        n += 1
    return fab_list


#版本３　迭代器处理
class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, (self.a + self.b)
            self.n += 1
            return r
        raise StopIteration()

    @staticmethod
    def get_fabs():
        for f in Fab(5):
            print f


if __name__ == "__main__":
    if False:
        fab(5)

    if False:
        print fab2(5)

    if True:
        Fab.get_fabs()
