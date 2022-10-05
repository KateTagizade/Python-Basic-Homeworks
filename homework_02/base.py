from abc import ABC
from homework_02 import exceptions

class Vehicle(ABC):
    def __init__(Self, weight = 10, started = "N", fuel = 40, fuel_consumption = 8):
        Self.weight = weight
        Self.started = started
        Self.fuel = fuel
        Self.fuel_consumption = fuel_consumption

    def start(Self):
         if Self.started == "N":
             if Self.fuel > 0:
                 return Self.started == "Y"
             raise exceptions.MyException("Нет топлива")
         print(Self.started)

    def move (Self, distance):
        if Self.fuel >= (int(Self.fuel_consumption)*int(distance)/100):
            return Self.fuel == (Self.fuel - (int(Self.fuel_consumption)*int(distance)/100))
        raise exceptions.MyException("Недостаточно топлива")

Vehicle1 = Vehicle(20,"N",10,50)


print(Vehicle1.start())
distance = 60

print(Vehicle1.move(60))

