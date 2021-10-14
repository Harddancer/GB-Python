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
    
    # поднимае в верхний регистр
    user=args.upper()
   
    # Парсим через объект класса response методом get,декодируем и сплитуем.
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    get_encod = response.encoding
    content = response.content.decode(get_encod)
    ls=re.split('</NumCode><CharCode>|</CharCode><Nominal>|</Name><Value>|</Value></Valute></ValCurs>|</Value></Valute><Valute',content)
    
    
    #Ищем дату, ковыряем заголовок и сплитуем, 
    #присваиваеми выводит через объъект дата
    fs = ls[0]
    date = re.split('<?xml version="1.0" encoding="windows-1251"?><ValCurs Date="|" name="Foreign Currency Market"><Valute ID="R01010"><NumCode>036',fs)
    a = str(date[0]).split('<?xml version="1.0" encoding="windows-1251"?><ValCurs Date="')
    a = a[1].split('.')
    day,mounth,year = a
    valute_data = datetime(year=int(year), month=int(mounth), day=int(day))
    
    
    # пишем ветвления опред элеменет по индексу, 
    #меняем запятую на точку переводим в float
    #выводим на экран
    if user in ls:
            val=ls[ls.index(user) + 2]
            val=val.replace(',','.')
            val=float(val)
            print(f'Валюта {user} равняется {val} рублей, курс на {valute_data}')
            
    else:
            print('Нет такой валюты')
currency_rate('usd')    

    

    
    