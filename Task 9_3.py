#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 18:16:02 2021

@author: yamamotod
"""
#
#       3. Реализовать базовый класс Worker (работник):
#    • определить атрибуты: name, surname, position (должность), income (доход);
#    • последний атрибут должен быть защищённым и ссылаться на словарь,
#    содержащий элементы «оклад» и «премия», 
#    например, {"wage": wage, "bonus": bonus};
#    • создать класс Position (должность) на базе класса Worker;
#    • в классе Position реализовать методы получения полного имени сотрудника 
#    (get_full_name) и дохода с учётом премии (get_total_income);
#    • проверить работу примера на реальных данных: создать экземпляры класса Position,
#    передать данные, проверить значения атрибутов, вызвать методы экземпляров.


class Woker:
    def __init__(self,name,surname,position,wage,bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'w':wage,'b':bonus}# публичная перменная,т.к. 
        #если сделать приватную то из функции main нет доступа
    
class Position(Woker):
    def get_fullname(self):
        return f'{self.name}  {self.surname}'
    def total_income(self):
        s = {sum(self.income.values())}
        return f'{s}'
    
    
def main():
    bruni = Position('ДЖАНИ', 'РОДАРИ', 'WRITER',100,1000)
    print(bruni.get_fullname(), bruni.position)
    print(bruni.total_income())

main()
    
    
    