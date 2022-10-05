"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class MyException(Exception):
    def __init__(self, text):
        self.txt = text


#LowFuelError = "Нет топлива"
#NotEnoughFuel = "Недостаточно топлива"
#CargoOverload = "Перегрузка"



