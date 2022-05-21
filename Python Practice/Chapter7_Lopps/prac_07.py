# FACTORIAL OF ANY NUMBER
# n! = 1X2X3X4X....n!



num = int(input("Enter Your Number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")
