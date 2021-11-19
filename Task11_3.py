#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 20:05:18 2021

@author: yamamotod
"""


class Digit (Exception):
    def init(self, txt):
        self.txt = txt

    
flag = 'ДА'
listing = []
    
while flag  == 'ДА':
    try:
        n = input('Введит целое число')
        if  int(n) < 0:
            
            raise Digit("Вы ввели не позитивное число!!!")
            flag = input('Вы хотите продолжить нажмите ДА')
    except ValueError:
                print("Вы ввели не число!")
                flag = input('Ва хотите продолжить  ДА  или НЕТ')
    except Digit as err:
                print(err)
                flag = input('Ва хотите продолжить  ДА  или НЕТ')
    else:
         listing.append(n)
         print('добавленно в список')
print(f"Ваш список: {listing}")
        

            
 
#inp_data = input("Введите положительное число: ")
#
#try:
#    inp_data = int(inp_data)
#    if inp_data < 0:
#        raise OwnError("Вы ввели отрицательное число!")
#except ValueError:
#    print("Вы ввели не число")
#except OwnError as err:
#    print(err)
#else:
#    print(f"Все хорошо. Ваше число: {inp_data}")       
#   
#   
#        
#        
#    
#    
#    
    
    
#        try:
#
#        if n is not digit:
#            raise Digit('Это не число')
#    
#    except (ValueError, Digit) as err:
#            print(err)
#            flag = input('Введите целое число')
#    else:
#            listing.append(n)
#            print(f"Все хорошо. Ваш список: {listing}")
#            break