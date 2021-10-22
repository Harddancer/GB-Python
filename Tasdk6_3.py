#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 22:01:29 2021

@author: yamamotod
"""


#Есть два файла: в одном хранятся ФИО пользователей сайта, 
#а в другом  — данные об их хобби.
#Известно, что при хранении данных используется принцип: 
#одна строка — один пользователь, разделитель между значениями — запятая.
#Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
#ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. 
#Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, 
#чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1». 
#При решении задачи считать,
#что объём данных в файлах 
#во много раз меньше объема ОЗУ.
import json
from itertools import zip_longest
with open('users.csv','r',encoding='utf-8') as u:
   us = u.read()
   with open('hobby.csv','r',encoding='utf-8') as h:
       hb = h.read()
       if len(u.readlines())>= len(h.readlines()):
           u.seek(0)
           h.seek(0)
           with open('file.csv','w',encoding='utf-8') as f:
               new_us = zip_longest((' '.join(i.split(',')) for i in u), (h for h in h),fillvalue=None)
               #print(*new_us)
               dictin = {str(i[0]).strip():str(i[1]).strip() for i in new_us}
               print(dictin)
       else:
           print('1')
           
with open('file.json','w',encoding='utf-8') as fj:
    json.dump(dictin,fj)
#import json
#num= 1.4
#print(type(num))
#num_js=json.dumps(1.4)
#print(type(num_js))
