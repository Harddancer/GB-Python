#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:51:38 2021

@author: yamamotod
"""

from sys import argv
u,h,file=argv[1:]
from itertools import zip_longest
with open('users.csv','r',encoding='utf-8') as u:
    with open('hobby.csv','r',encoding='utf-8') as h:
        with open('file2.txt','w',encoding='utf-8') as file:       
               new_us = zip_longest(u,h)
               for i in new_us:
                   dictin = {str(i[0]).strip():str(i[1]).strip()}
                   print(dictin)