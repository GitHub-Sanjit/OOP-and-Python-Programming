class Calculator:
    brand = "Casio MS990"

    def add(self, num1, num2):
        return num1 + num2

    def deduct(self, num1, num2):
        return num1 - num2

    def mult(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2


calc = Calculator()
print(calc.add(10,5))
print(calc.deduct(10,5))
print(calc.mult(10,5))
print(calc.divide(10,5))