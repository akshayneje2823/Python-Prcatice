# WRITE A OROGRAM TO FIND WHEATHER A GIVEN NUMBER IS PRIME OR NOT


num = int(input("Enter Your Number: "))
prime = True

for i in range(2, num):
    if(num%i == 0):
        prime = False 
        break
if prime:
    print("Prime number")
else:
    print("Not Prime number")
