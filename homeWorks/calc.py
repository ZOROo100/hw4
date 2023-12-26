class Calculator:
    def __init__(self, num1 , num2):
        self.num1 = num1
        self.num2 = num2


    def __add__(self):
        return self.num1 + self.num2

    def __sub__(self):
        return self.num1 - self.num2

    def __mul__(self):
        return (self.num1 * self.num2)

    def __truediv__(self):
        return self.num1 / self.num2

a = Calculator(num1 = 1, num2 = 2)

print(a.__add__())