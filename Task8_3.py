#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 22:02:49 2021

@author: yamamotod
"""


#Написать декоратор для логирования 
#типов позиционных аргументов функции, например:
#def type_logger...
#    ...
#
#
#@type_logger
#def calc_cube(x):
#   return x ** 3
#
#
#>>> a = calc_cube(5)
#5: <class 'int'>
#
#
#Примечание: если аргументов несколько - 
#выводить данные о каждом через запятую; 
#можете ли вы вывести тип значения функции? 
#Сможете ли решить задачу для именованных аргументов? 
#Сможете ли вы замаскировать работу декоратора? 
#Сможете ли вывести имя функции, например, в виде:
#>>> a = calc_cube(5)
#calc_cube(5: <class 'int'>)

#import urllib
#resource = 'http://www.python.org'
#with urllib.request.urlopen(resource) as s:
#    print(s.read())
def type_logger(func):
    @wraps(func) # прячем вывод обертки
    def wrapper(*args):
        pos = [i for i in (*args)]
        p = [f'{func.__name__}({i}:{type(i)})'for i in pos]
        print(*p,*func(*args))
    return wrapper
            
            
    

@type_logger
def cube(*args):
    l = [i  for i in args if str(i).isdigit()]
    c = list(map(lambda x: int(x)**3, l))
    print(list(c))
    return c
cube(1,2, 8, 9, 67,8)    
  

    
