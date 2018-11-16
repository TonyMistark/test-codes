#!/usr/bin/env python
# encoding: utf-8

from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print("Process to write: %s" % os.getpid())
    for value in ["A", "B", "C"]:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print("Process to read: %s" % os.getpid())
    while True:
        value = g.get(True)
        print("Get %s from queue." % value)


if __name__ == "__main__":
    q = Queue()
    pw = Process(taget=write, args=(q, ))
    pr = Process(taget=read, args=(q, ))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    pr.terminate()



