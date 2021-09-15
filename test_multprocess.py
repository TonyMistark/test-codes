import time
from threading import Thread


def decoretor(f):
    def wrapper(*args, **kw):
        start = time.time()
        func = f(*args, **kw)
        end = time.time()
        print(f"cost: {end - start}")
        return func
    return wrapper


def demo1(n):
    flag = True
    for i in range(n):
        flag = not flag
    print("end")


@decoretor
def test1(n):
    print("Single thread")
    demo1(n)
    demo1(n)

test1(int(1e9))



@decoretor
def test2(n):
    print("Two thread with python threading library")
    t1 = Thread(target=demo1, args=(n,))
    t2 = Thread(target=demo1, args=(n,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

test2(int(1e9))
