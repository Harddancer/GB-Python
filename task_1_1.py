#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 23:11:55 2021

@author: yamamotod
"""


# Реалтзовать вывод информации  о промежутке времени 
# в зависимости от его продолжительности  duration  в секундах.
def duration_date():
    choice = 'да'
    while choice == 'да' or choice == 'Да':
        try:
            duration = int(input('введите расстояние целое число'))
        
  
            if duration <= 59:
                sec = duration
                print(sec, 'сек')
            elif (duration // 60) < 60:
                minut = duration // 60 
                sec = duration % 60
                print(minut, 'мин', sec, 'сек')
            elif duration // 60 > 60 and duration // 60 < 1440:
                hours = duration // 3600 
                minut =(duration % 3600)//60
                sec = (duration % 3600) % 60
                print(hours,'час',minut, 'мин', sec, 'сек') 
            elif (duration // 60) >= 1440: 
                day = duration // 86400
                remains = duration  % 86400
                new_hours = remains // 3600
                remains = remains  % 3600
                minut = remains // 60
                sec = remains % 60
                print(day, 'дней', new_hours,'час',minut, 'мин', sec, 'сек')   
            else:
                print('Попробуй еще раз')
            choice = input('Введите Да или да чтоб продолжить или НЕТ чтоб выйти ')
            if choice == 'НЕТ':
                break
            else:
                continue
    
        except ValueError:
            print('не корректный ввод')
    
duration_date()
