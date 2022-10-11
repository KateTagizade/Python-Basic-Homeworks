"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02 import base
import homework_02.exceptions

class Plane (base.Vehicle):
    cargo = 0
    def __init__(self, weight=10, fuel=40, fuel_consumption=8,max_cargo=11):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        if (self.cargo+cargo)<=self.max_cargo:
            self.cargo+=cargo
            return
        raise homework_02.exceptions.CargoOverload

    def remove_all_cargo (self):
        cargo = self.cargo
        self.cargo = 0
        return cargo

if __name__=="__main__":
    Plane().load_cargo(10)