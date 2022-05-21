class Calaculator:
    
    def __init__(self, num):
        self.number = num
    
    def square(self):
        print(f"the square root of {self.number} this number is {self.number**2}")

    def squareRoot(self):
        print(f"the squareRoot root of {self.number} this number is {self.number**0.5}")

    def cube(self):
        print(f"the square cube of {self.number} this number is {self.number **3}")
    
    @staticmethod
    def greet():
        print("Hello, Good morning")

a = Calaculator(9)
a.square()
a.squareRoot()
a.cube()
a.greet()