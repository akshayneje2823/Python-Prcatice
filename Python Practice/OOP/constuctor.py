
class Employee:
    company = "Google"

    def __init__(self, name, salary,id):
        self.name = name
        self.salary = salary
        self.id = id
        print("Employee is created!")
        
    def getDetails(self):
        print(f'name is {self.name}')
        print(f'salary is {self.salary}')
        print(f'id is {self.id}')

    def getsalary(self):
        print(f"salary for employee working in {self.company} is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning, sir")       

harry = Employee("Akshay",40000,101)
harry.getDetails()
    