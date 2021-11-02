#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 17:53:46 2021

@author: yamamotod
"""


import time


class TrafficLight:
    __color = 'red'
    

    def running(self):
        count = 0
        while count < 10:
            print('UP')
            count += 1

            self.__color = 'red'
            print(f'цвет: {self.__color}')
            time.sleep(7)
            count += 1
            
            self.__color = 'yellow'
            print(f'цвет: {self.__color}')
            time.sleep(2)
            count += 1

            self.__color = 'green'
            print(f'цвет: {self.__color}')
            time.sleep(3)
            count += 1


def main():
    traff_light = TrafficLight()
    print(traff_light.running())
    
main()