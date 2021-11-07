#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 16:55:44 2021

@author: yamamotod
"""


#Реализовать проект расчёта суммарного расхода ткани на производство одежды.
#Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
#К типам одежды в этом проекте относятся пальто и костюм.
#У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
#Это могут быть обычные числа: V и H соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: 
#для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
#Проверить работу этих методов на реальных данных.
#Выполнить общий подсчёт расхода ткани. 
#Проверить на практике полученные на этом уроке знания.
#Реализовать абстрактные классы для основных классов проекта и
#проверить работу декоратора @property.

from abc import ABC, abstractmethod
class Clothes(ABC):
    pass

    @abstractmethod
    def itog(self):
        pass
        
    def __add__(self,other):
        return self.itog + other.itog

class Coat(Clothes):
    def __init__(self,size):
        self.size = size
     
    @property   
    def size(self):
        return self.size
    
    @size.setter
    def size(self,size):
        if size < 30:
            self.size = 30
        elif size > 60:
            self.size = 60
        else:
            self.size = size
            
    @property
    def itog(self):
        return self.size/6.5 + 0.5
    
    
    
class Shirt(Clothes):
    def __init__(self,hight):
        self.hight = hight
     
    @property   
    def hight(self):
        return self.hight
    
    @hight.setter
    def hight(self,hight):
        if hight < 30:
            self.hight = 30
        elif hight > 60:
            self.hight = 60
        else:
            self.hight = hight
            
    @property
    def itog(self):
        return self.hight*2 +0.3
    
coat = Coat(20)
print(coat.itog)
shirt = Shirt(20)
print(shirt.itog)
    
        
    
    
        
        
    