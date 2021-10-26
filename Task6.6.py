#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:52:55 2021

@author: yamamotod
"""
from sys import argv

def add_sale(argv):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
            for line in argv[1:]:
                f.write(argv[0])
                f.write(' ' + line + '\n')
                print(f'файл записан')
        
add_sale(argv[0:])
        

from sys import argv

def read_sale(argv):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if len(argv) == 3:
            r = [i for i in argv[1:] if i.isdigit()]
            print(r)
            x,y = map(int,(e for e in r))
            #print(x,y)
            print(*(v for i,v in enumerate(f) if x-1 <= i < y))
#       
        elif len(argv) == 2:
            r = [i for i in argv[1:] if i.isdigit()]
            x = int(*r)
            print(*(v for i, v in enumerate(f) if i >= x - 1))
        else:
            print(f.read())
read_sale(argv)             
        
        
        
        

       