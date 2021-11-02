#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 14:32:40 2021

@author: yamamotod
"""


import re
def email_parse(string):
    email = re.compile(r"(?P<username>[a-zA-Z0-9\_\-\.]+).(?P<domain>[a-zA-Z0-9\_\-\.]+)")
    # делаем шаблон регулярного выражения с именнованными подгруппами (?P)
    if not email.match(string):
        # делаем ветвление и применяем объект match библиотека re  для сравнения шаблона и исх строки
        
         raise ValueError(f'wrong email {string}')
         # вызываем исключение raise  с ошибкой VE  применяем f-строки для вывода
    else:
        print(email.match(string).groupdict())
        # выводим на экран шаблон с объктом match параметр исх строка с методом groupdict
        
email_parse("yamamotod@mail.ru") 
#вызываем функцию 

