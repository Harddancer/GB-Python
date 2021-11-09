#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 14:47:35 2021

@author: yamamotod
"""

class Cell:
    def __init__(self,num):
        self.num = num
       
    
    def __add__(self, other):
        if isinstance(other, Cell):
            return Cell(self.num + other.num)
        elif isinstance(other, int):
            return Cell(self.num + other)
        else:
            return NotImplemented
    
    def __sub__(self, other):
        return Cell(self.num - other.num)
    
    def __mul__(self, other):
        return Cell(self.num * other.num)
    
    def __floordiv__(self, other):
        return Cell(self.num // other.num)
    
    def __str__(self):
        return str(self.num)
    
    
    def make_order(self, r):
        return '\n'.join(['$' * r for i in range(self.num // r)]) + '\n'\
    + '$' * (self.num % r)
        
        
    
     
    
    
    
    
a = Cell(9)
b = Cell(67)
print(a+b)
print(b.make_order(3))

    
    
    

