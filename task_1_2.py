#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 19:03:05 2021

@author: yamamotod
"""


def number_cub():  #Создать список, состоящий из кубов нечётных чисел от 1 до 1000
    number = []
    for i in range(1, 1001):
        if i % 2 != 0:
            i = i**3
            number.append(i)
           
        else:
            None
    #print(number)
    return number


def number_summ(): #Вычислить сумму тех чисел из этого списка, 
                   #сумма цифр которых делится нацело на 7
    number_s = 0     
    for i in range(len(number_cub())):
        n = number_cub()[i]
        accum = 0
        while n > 0:
            accum += n % 10
            n = n // 10
        if accum % 7 == 0:
            number_s += number_cub()[i]
    print(number_s)
    return number_s
     
number_summ()    
    
    
def number_summ():#К каждому элементу списка добавить 17 и заново вычислить сумму 
                  #тех чисел из этого списка, сумма цифр которых делится нацело на 7.
    number_s = 0     
    for i in range(len(number_cub())):
        n = number_cub()[i] + 17
        accum = 0
        while n > 0:
            accum += n % 10
            n = n // 10
        if accum % 7 == 0:
            number_s += number_cub()[i]
    print(number_s)
    return number_s
     
number_summ() 