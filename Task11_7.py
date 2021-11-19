#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 20:05:26 2021

@author: yamamotod
"""
# Вариант 0. Использование встроенного типа данных complex:<br>
class Complex:
    def __init__(self, num, compl):
        self.num = num
        self.compl = compl

    def __str__(self):
        return f'{self.num}+{self.compl}i' if self.compl > 0 else f'{self.num}{self.compl}i'

    def __add__(self, other):
        return Complex(self.num + other.num, self.compl + other.compl)

    def __mul__(self, other):
        return Complex((self.num * other.num - self.compl * other.compl),
                             (self.num * other.num + self.compl * other.compl))


cn = Complex(4, -2)
cn1 = Complex(9, 4)
print(cn + cn1)
print(cn * cn1)
print(complex(1, -5) * complex(1, 2))  

# Вариант 1. Использование встроенного типа данных complex

a = input()
b = input()
a = complex(a)
b = complex(b)
suma = a + b
mult = a * b
print(suma)
print(mult)



#