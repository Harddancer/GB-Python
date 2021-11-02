#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:01:00 2021

@author: yamamotod
"""

#
#    4. Реализуйте базовый класс Car:
#    • у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#    А также методы: go, stop, turn(direction), которые должны сообщать, 
#    что машина поехала, остановилась, повернула (куда);
#    • опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#    • добавьте в базовый класс метод show_speed, который должен показывать 
#    текущую скорость автомобиля;
#    • для классов TownCar и WorkCar переопределите метод show_speed. 
#    При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
#    должно выводиться сообщение о превышении скорости.

class Car:
    def init(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} двигается')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self):
        print(f'Автомобиль {self.name} повернул в неизвестном направлении')

    def show_speed(self):
        return f'Автомобиль {self.name} двигается со скоростью {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Автомобиль {self.name} двигается со скоростью {self.speed} км/ч.' 
        else:
            f' Превышение! {super().show_speed()}'
           
            
        
        
       
class WorkCar(Car):
    def show_speed(self):
        return f'Автомобиль {self.name} двигается со скоростью {self.speed} км/ч.' \
               f' Превышение установленной скорости движения!' if self.speed > 40 else super().show_speed


class SportCar(Car):
    """Спортивная машина"""


class PoliceCar(Car):
    Car.is_police = True


town_car = TownCar(70, 'Белый Белый', 'Audi')
work_car = WorkCar(60, 'Баклажан', 'Белаз')
sport_car = SportCar(180, 'Малиновый', 'Bugatti')
police_car = PoliceCar(150, 'Голубая волна', 'LADA')

cars = [town_car, work_car, sport_car, police_car]
for val in cars:
    val.go()
    print(val.color)
    print(val.show_speed())
    val.turn()
    val.stop()
   