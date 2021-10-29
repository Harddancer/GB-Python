#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 00:18:20 2021

@author: yamamotod
"""


#import re
#def email_parse(string):
#    #string  = "yamaqQQQmo_todW1-98876544@mail.ru"
#    
#    r = re.compile(r"([a-zA-Z0-9\_\-\.]+)")
#    f = re.findall(r, string)
#    if not r.match(string):
#         raise ValueError(f'wrong email {string}')
#    else:
#        a=['username','domain']
#        d =dict(zip(a,f))
#        print(f'Ваша почта {string} верна \n {d}')
#        
#        
#email_parse("yamamotod@mail.ru") 


#
#import re
#string  = "yamaqQQQmo_todW1-98876544@mail.ru"
#m = re.match(r"(?P<username>\w+) (?P<domain>\w+)", "string")
#r= re.match.groupdict()
print(dir(re.match))