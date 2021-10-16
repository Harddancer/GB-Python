#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 21:31:43 2021

@author: yamamotod
"""


#Представлен список чисел. Необходимо вывести те его элементы, 
#значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]


#Подсказка: использовать возможности python, изученные на уроке.
#Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
import sys

result = (src[i] for i in range(0, len(src)) if src[i] > src[i-1])
for i in result:
    print(i,sys.getsizeof(i))

