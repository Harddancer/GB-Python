#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 23:13:52 2021

@author: yamamotod
"""


#Склонение слова
#Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой 
#для каждого из чисел в интервале от 1 до 100:
#1 процент
#2 процента
#3 процента
#4 процента
#5 процентов
#6 процентов
#...
#100 процентов
word = ['процентов','процент', 'процента']

for w in range(1,101):
    if w % 100 >= 11 and w % 100 <=14:
        print(str(w) + word[0])
    elif w % 10 == 1:
        print(str(w) + word[1])
    elif w % 10 >= 2 and w % 10 <=4:
        print(str(w) + word[2])
    else:
        print(str(w) + word[0])