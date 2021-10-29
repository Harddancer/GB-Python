#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:50:47 2021

@author: yamamotod
"""
import re
# запись
#with open('new_nginx_logs.txt', 'w', encoding='utf-8') as file:
#    with open('nginx_logs.txt', encoding='utf-8') as f:
#        ls = ((l.split(' ')[0], l.split(' ')[5][1:], l.split(' ')[6]) for l in f)
#        for i in ls:
#            print(i,file=file)
            
import collection
with open('new_nginx_logs.txt',  encoding='utf-8') as file:
    dictin = collection.Counter()
    for i in file:
        i=i.split()[0]
        dictin += 1
    ip, count = dictin.most_common(1)[0][0], dictin.most_common(1)[0][1]
    print(f"Spammer {ip} {count}")
       
    


  
    
    
  