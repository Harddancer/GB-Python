#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 20:23:07 2021

@author: yamamotod
"""

from requests import get
import re
from datetime import datetime
datetime_now = datetime.now()


def currency_rate(args):
    #user = 'usd'
    user=args.upper()
   

    #def currency_rate(valut):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    get_encod = response.encoding
    #print(get_encod)
    #encod = response.encoding = 'utf-8' 
    content = response.content.decode(get_encod)
    #print(content)
    #print(type(content))
    ls=re.split('</NumCode><CharCode>|</CharCode><Nominal>|</Name><Value>|</Value></Valute></ValCurs>|</Value></Valute><Valute',content)
    #print(ls)
    fs = ls[0]
    #print(fs)
    date = re.split('<?xml version="1.0" encoding="windows-1251"?><ValCurs Date="|" name="Foreign Currency Market"><Valute ID="R01010"><NumCode>036',fs)
    a = str(date[0]).split('<?xml version="1.0" encoding="windows-1251"?><ValCurs Date="')
    #a = str(a).split('<?xml version="1.0" encoding="windows-1251"?><ValCurs Date="')
    a = a[1].split('.')
    #a = a.split('.')
    day,mounth,year = a
    print(f'{day} {mounth} {year}')
    
   
    if user in ls:
            val=ls[ls.index(user) + 2]
            val=val.replace(',','.')
            val=float(val)
            print(type(val))
            print(user,val)
            print(datetime_now)
    else:
            print('Нет такой валюты')
currency_rate('usd')    

    

    
    