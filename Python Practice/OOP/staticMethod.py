# class Employee:
#     company = "Google"
#     def getsalary(self):
#         print(f"salary for employee working in {self.company} is {self.salary}")

#     def greet(self):
#         print("Good Morning, sir")       

# akshay =Employee()
# akshay.salary = 40000
# akshay.getsalary()
# akshay.greet()

class Employee:
    company = "Google"
    def getsalary(self):
        print(f"salary for employee working in {self.company} is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning, sir")       

akshay =Employee()
akshay.salary = 40000
akshay.getsalary()
akshay.greet()