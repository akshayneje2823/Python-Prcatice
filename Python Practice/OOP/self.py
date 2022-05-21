# SELF -->
# SELF REFERS TO THE INSATNCE OF THE CLASS
# IT IS AUTOMATICALY PASSED WITH A FUCTION CALL FROM AN OBJECT


# class Employee:
#     company = "Google"
#     def getsalary(self):
#         print("salary is 100k")

# akshay =Employee()
# akshay.getsalary()
# Employee.getsalary(akshay)  

class Employee:
    company = "Google"
    def getsalary(self):
        print(f"salary for employee working in {self.company} is {self.salary}")

akshay =Employee()
akshay.salary = 40000
akshay.getsalary()

# Employee.getsalary(akshay) 