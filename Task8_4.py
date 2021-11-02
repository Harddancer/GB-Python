#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 19:12:42 2021

@author: yamamotod
"""


def valcheker(funckes):
    def val_cheker(funck):
        def wrapper(c):
            if funckes(c):
                print(funck(c))
            else:
                raise ValueError('значение не то', c)
        return wrapper
    return val_cheker
@valcheker(lambda i: i > 0)
def cube(i):
    return i**3

try:
    cube(3)
    print(cube)
except (ValueError) as e:
    print(e)
