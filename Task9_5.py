#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:31:04 2021

@author: yamamotod
"""
#
##    5. Реализовать класс Stationery (канцелярская принадлежность):
##    • определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
##    • создать три дочерних класса Pen (ручка), 
#Pencil (карандаш), Handle (маркер);
##    • в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
##    • создать экземпляры классов и проверить, 
#что выведет описанный метод для каждого экземпляра.
class Stationery:
    def __init__(self, title='нечто'):#метод конструктор
        self.title = title# переменая паблик для связи с подклассами насследования

    def draw(self):
        print(f'рисуем {self.title}') # метод


class Pen(Stationery):# подкласс
    def draw(self):
        print(f'pen {self.title}')


class Pencil(Stationery):# подкласс
    def draw(self):
        print(f'pencil {self.title}')


class Handle(Stationery):# подкласс
    def draw(self):
        print(f'marker {self.title}')

def main():
    stat_draw = Stationery()# создаем объект(экземпляр класса Stationery
    pen = Pen('guliver')
    pencil = Pencil('NOOR')
    marker = Handle('cisco')


    a = [stat_draw, pen, pencil, marker]
    for val in a:
        val.draw()
main()