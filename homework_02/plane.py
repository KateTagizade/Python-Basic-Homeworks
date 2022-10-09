"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02 import base

class Plane (base.Vehicle):
    cargo = 10
    def __init__(self, weight=10, fuel=40, fuel_consumption=8,max_cargo=11):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    mycargo = 15
    def load_cargo(self, cargo, mycargo):
        if (cargo+mycargo)<=self.max_cargo:
            cargo+=mycargo
        raise exceptions.CargoOverload


    def remove_all_cargo (self):
        a = 0
        self.cargo = a
        self.cargo = self.cargo - self.mycargo
