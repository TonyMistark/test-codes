#!/usr/bin/env python
# encoding: utf-8

from memory_profiler import profile

test_num = 1000000

@profile
def test_profile():
    test_list = ["a"]
    t = xrange(test_num)
    test_list.extend(t)
    test_list.append("a")

@profile
def test_profile2():
    test_list = ["b"]
    t = range(test_num)
    test_list.extend(t)
    test_list.append("b")

if "__main__" == __name__:
    range(test_num)
    #xrange(test_num)
    test_profile2()
    test_profile()
