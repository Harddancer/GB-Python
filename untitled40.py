#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 16:19:40 2021

@author: yamamotod
"""


class Data:

       
    @classmethod
    def mod(cls, ds):
        d,m,y = map(int, ds.split('-'))
        return (d,m,y)
       
    
    @staticmethod
    def validation(ds):
        d,m,y = map(int, ds.split('-'))
        if d < 31 and m < 12 and y < 1999:
            return  f'День {d} Месяц {m}  Год {y}'
        else:
            print('Некорректная дата')
        

        

print(Data.validation('11-5-1986'))
    



