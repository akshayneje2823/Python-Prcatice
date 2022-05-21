# create a program for storing information of few programmers working at microsoft

class Programer:
    company = "Microsoft"
    def __init__(self, name, product): 
        self.name = name
        self.product = product

#     def getInfo(self):
#         print(f"The name of the progamer from {self.company} company is {self.name} and product is {self.product}")

# darshan = Programer("Darshan","Java")
# deeepak = Programer("deepak","python")
# darshan.getInfo()
# deeepak.getInfo()

harry = Programer("Harry", "Javscript")
print(harry)