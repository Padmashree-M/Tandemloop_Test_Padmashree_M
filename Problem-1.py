# Problem-1.py
class Calculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b == 0:
            return "Error: Division by zero"
        return self.a / self.b

def main():
    try:
        a = float(input("Enter a (double): ").strip())
        b = float(input("Enter b (double): ").strip())
        op = input("Enter operation (add/sub/mul/div or + - * /): ").strip().lower()
        calc = Calculator(a, b)
        if op in ("add", "+", "addition"):
            print(calc.add())
        elif op in ("sub", "-", "subtract"):
            print(calc.sub())
        elif op in ("mul", "*", "multiply"):
            print(calc.mul())
        elif op in ("div", "/", "divide"):
            print(calc.div())
        else:
            print("Invalid operation")
    except ValueError:
        print("Invalid numeric input")

if __name__ == "__main__":
    main()
