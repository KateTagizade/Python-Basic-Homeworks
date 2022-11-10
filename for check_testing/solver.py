class Solver:
    PARAMS_TYPE_EXC_TEXT = "values should be nums!"
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        #return
        return self.a + self.b

    def mul(self):
        if not all((
            isinstance(self.a, (int, float)),
            isinstance(self.b, (int, float)),
        )):
            raise TypeError(self.PARAMS_TYPE_EXC_TEXT)
        return self.a * self.b