#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 18:07:39 2021

@author: yamamotod
"""

from time import perf_counter
import sys
start = perf_counter()
numbers =(num for num in range(1,int(input('число'))+1,2))
print(*numbers, sys.getsizeof(numbers))
print(perf_counter()-start)
print(type(numbers))
#print(next(numbers))
print(start,perf_counter())



print(*(num for num in range(1,int(input('число'))+1,2)))# генератор
print(*[num for num in range(1,int(input('число'))+1,2)])# comprehensions