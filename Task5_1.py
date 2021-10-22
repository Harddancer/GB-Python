#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 15:07:50 2021

@author: yamamotod
"""


#Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield, например:
#>>> odd_to_15 = odd_nums(15)
#>>> next(odd_to_15)
#1
#>>> next(odd_to_15)
#3
#...
#>>> next(odd_to_15)
#15
#>>> next(odd_to_15)
#...StopIteration...
import sys
n = int(input('число'))
def numbers(n):
    
    for i in range(1,n+1,2):
        yield i
for i in numbers(n):
    print(i,sys.getsizeof(i))
    #print(next(i))# заканчивается итерация, перебирать больше нечего
num = numbers(n)

   
       
# 
#import sys
#def numbers(n):
#    num =[]
#    for i in range(1,n+1,2):
#        num.append(i)
#        return num
#num = numbers(8)
#print(type(num),sys.getsizeof(num))
#
#
#
#def letters_generator(start, end):
#   for code in range(ord(start), ord(end) + 1):
#       yield chr(code)
#
#
#eng_uppercase_letters = letters_generator('A', 'Z')
#print(*eng_uppercase_letters, sep='')  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
#
##list comprehension
#nums_cube_gen = (num ** 3 for num in range(5 + 1))
#print(type(nums_cube_gen), *nums_cube_gen)
## <class 'generator'> 0 1 8 27 64 125
#
##А если нам в алгоритме нужен список? Можем выполнить преобразование:
#nums_cube_gen = (num ** 3 for num in range(5 + 1))
#nums_cube = list(nums_cube_gen)
#print(type(nums_cube), nums_cube)
## <class 'list'> 0 1 8 27 64 125
#
#nums_cube = {num: num ** 3 for num in range(1, 5 + 1)}
#print(nums_cube)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
#
#import random
#
#random_nums = {random.randint(1, 100) for _ in range(10)}
#print(len(random_nums), random_nums)



