#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 15:07:32 2021

@author: yamamotod
"""

    
def num_translate_adv(num):
    """ Функция словарь"""

    dict_num = {'one': 'один',
                'two': 'два',
                'tree': 'три',
                'four': 'четыре',
                'five': 'пять',
                'six': 'шесть',
                'seven': 'семь',
                'eight': 'восемь',
                'nine': 'девять',
                'ten': 'десять'}
    if  num in dict_num.keys():
        print(dict_num.get(num, 'Нет'))
    elif num in dict_num.keys() and num.isupper:
        print(dict_num.get(num.capitalize(), 'Нет'))
    else:
        None
num_translate_adv('')
