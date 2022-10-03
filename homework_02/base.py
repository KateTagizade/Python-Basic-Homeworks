from abc import ABC
#from homework_02 import exceptions

class Vehicle(ABC):
    def __init__(self, weight = 10, started = 0, fuel = 100, fuel_consumption = 5):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self, Vehicle):
         if self.started == 0:
             if self.fuel > 0:
                 return self.started == 1
             raise LowFuelError ("Недостаточно топлива")
         print(self.started)

Vehicle1 = Vehicle(0,100,5)

