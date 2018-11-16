#!/usr/bin/env python
# encoding: utf-8

import random
import string

def generate_activation_code(len=16, n=200):
    '''生成n个长度为len的随机序列码'''
    random.seed()
    chars = string.ascii_letters + string.digits
    return [''.join([random.choice(chars) for _ in range(len)]) for _ in range(n)]
    if __name__ == '__main__':
        for index, code in enumerate(generate_activation_code(), 1):
            print(index, code)

