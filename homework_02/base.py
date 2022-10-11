from abc import ABC
import homework_02.exceptions

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
             raise homework_02.exceptions.LowFuelError

    def move (self, distance):
        if self.fuel >= distance*self.fuel_consumption:
            self.fuel -= distance*self.fuel_consumption
            return
        raise homework_02.exceptions.NotEnoughFuel

if __name__=="__main__":
    Vehicle1: Vehicle = Vehicle(20,0,50)
    print(Vehicle1.start())
    print(Vehicle1.started)
#distance = 60

#print(Vehicle1.move(60))

