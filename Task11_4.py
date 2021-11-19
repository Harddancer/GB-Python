#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 11:19:49 2021

@author: yamamotod
"""


class Warehouse:
    def __init__(self, *subjects):# передаем список имен техники 
        self.subjects = list(subjects)
    def my_list(self): 
        return self.subjects# метод возвращает список
    
    def __str__(self):
        return f'Cписок поступлений {self.subjects}'  # выводим объект
    # Warehouse в строком виде  
  
  
        
class Office_equipment:# создаем класс оргтехника
    def __init__(self,name,types):
        self.name = name
        self.types = types
        
    def __str__(self):
        return f'Cписок поступлений {self.name}  {self.types}' # выводим объект
    # Office equipment в строком виде  
        
class Scaner(Office_equipment):# создаем классу техникни
    #наследование от род класса 
    def __init__(self,name):
        super().__init__(name)
        
class Printer(Office_equipment): #создаем классу техникни
    #наследование от род класса 
    def __init__(self, name):
        
        super().__init__(self,name) 
        self.knowledges = [] 
    def add (self, name):# создаем метод добавления объекта Printer  в список
  
            self.knowledges = []
            self.knowledges.append(name + '1')
            return self.knowledges
      
#HP = Printer('HP','MFU')  
#print(HP) 
#print(HP.to_take('ABRACADABRA'))
s = Warehouse('HP','Samsung')  
p_1 = Printer('HP')# создаем объект от класса Printer
p_2 = Printer(' Brother')# создаем объект от класса Printer
print(p_1.add('HP'))# вызываем метод add класса Printer
print(p_2.add('Brother')) # вызываем метод add класса Printer
print(s)
        
        
       
    