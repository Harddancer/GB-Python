#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 16:37:17 2021

@author: yamamotod
"""


#Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
#>>> thesaurus("Иван", "Мария", "Петр", "Илья")
#{
#    "И": ["Иван", "Илья"], 
#    "М": ["Мария"],
#    "П": ["Петр"]
#}

#Подумайте: полезен ли будет вам оператор распаковки? 
#Как поступить, если потребуется сортировка по ключам? 
#Можно ли использовать словарь в этом случае?



def thesaurus(*args):
    name = list(args)
    alfa = [] 
    for i in args:
        letter_name = i[0]
        alfa.append(letter_name)
        name = list(args)
    names_dict = dict(zip(alfa,name))
    return names_dict

print(thesaurus('Железякин','Веревкин','Cтеклов'))
   

        
        
        
    
    


    