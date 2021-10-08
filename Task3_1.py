#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 12:22:52 2021

@author: yamamotod
"""


#Написать функцию num_translate(), 
#переводящую числительные от 0 до 10 c английского на русский язык. Например:
#>>> num_translate("one")
#"один"
#>>> num_translate("eight")
#"восемь"
#Если перевод сделать невозможно, вернуть None. 
#Подумайте, как и где лучше хранить информацию, 
#необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

def num_translate(num):
    
    """
    
    Функция словарь
    
    :in numbers
    : out words
    
    """
        
    dict_num= { 'one':'один',
               'two':'два',
               'tree':'три',
               'four':'четыре',
               'five':'пять',
               'six':'шесть',
               'seven':'семь',
               'eight':'восемь',
               'nine':'девять',
               'ten':'десять'}
    num in dict_num.keys() == True
    print(dict_num.get(num, 'Нет'))
num_translate('nine')


print(help(num_translate))
    
        
    