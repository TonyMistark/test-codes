#!/usr/bin/env python
# encoding: utf-8

from memory_profiler import profile


@profile
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1

@profile
def main():
    for n in fab(100):
        print n
        n

if __name__ == "__main__":
    main()
