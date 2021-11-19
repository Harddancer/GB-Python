#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 20:24:27 2021

@author: yamamotod
"""


class Warehouse:

    def __init__(self, *subjects):# передаем список имен техники
      self.subjects = {k: [] for k in subjects} 

    def my_list(self):
        return self.subjects
       
         
       

    def __str__(self):
        for k, v in self.subjects.items(): 
            if k != k.isdigit():
                return f'Cписок поступлений {self.subjects}'  # выводим объект
    # Warehouse в строком виде
            else:
                print('что то не то')


class Office_equipment:  # создаем класс оргтехника
    def __init__(self, name, types):
        self.name = name
        self.types = types

    def __str__(self):
        return f'Cписок поступлений {self.name}  {self.types}'  # выводим объект
    # Office equipment в строком виде


class Scaner(Office_equipment):  # создаем классу техникни
    # наследование от род класса
    def __init__(self, name, types="Scanner"):
        super().__init__(name, types)


class Printer(Office_equipment):  # создаем классу техникни
    # наследование от род класса
    def __init__(self, name, types="Printer"):
        super().__init__(name, types)


# HP = Printer('HP','MFU')
# print(HP)
# print(HP.to_take('ABRACADABRA'))
s = Warehouse('Scanner', 'Printer')
p_1 = Printer('HP')  # создаем объект от класса Printer
p_2 = Printer(' Brother')  # создаем объект от класса Printer
#print(s.my_list())
s.subjects[p_1.types].append(p_1.name)  # вызываем метод add класса Printer
s.subjects[p_2.types].append(p_2.name)  # вызываем метод add класса Printer
#print(s.my_list())
print(s)






