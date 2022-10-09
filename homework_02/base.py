from abc import ABC
from homework_02 import exceptions

class Vehicle(ABC):
    started:bool = False
    def __init__(self, weight = 10, fuel = 40, fuel_consumption = 8):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
         if not self.started:
             if self.fuel > 0:
                self.started = True
                return
             raise exceptions.LowFuelError

    def move (self, distance):
        if self.fuel >= ((self.fuel_consumption*distance)/100):
            self.fuel = ((self.fuel) - (self.fuel_consumption)*distance/100)
        raise exceptions.NotEnoughFuel

#if __name__=="__main__":
#    Vehicle1: Vehicle = Vehicle(20,0,50)
#    print(Vehicle1.start())
#    print(Vehicle1.started)
#distance = 60

#print(Vehicle1.move(60))

