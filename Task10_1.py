#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 15:54:08 2021

@author: yamamotod
"""



from itertools import zip_longest

class Matrix:
    def __init__(self, array):
        self.array = array
        
    def __str__(self):

        return f' {self.array}'
    
    def __add__(self, other):
        a = [t for t in zip_longest (self.array,other.array,fillvalue = 0)]
        for a in a:
            return Matrix([map(sum, (zip_longest(*a, fillvalue=0)))])
#    
s1 = Matrix([[1,2],[3,4], [5,6]])
s2 = Matrix ([[1,2],[3,4], [5,6]])
print(s1 + s2)

#q = [[1,2],[3,4], [5,6],[6,6]]
#v = [[1,2],[3,4], [5,6]]
#a = [t for t in zip_longest (q,v,fillvalue = 0)]
#print(a)
#print( [map(sum, (zip_longest(a, fillvalue=0)))] )

