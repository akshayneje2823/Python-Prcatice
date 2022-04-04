# WRITE A PROGRAM TO ACEEPT THE MARKS OF 6 SUITABLE AND DISPLAY THEM IN SORTED METHOD

m1 = int(input("Enter Students Mark 1: "))
m2 = int(input("Enter Students Mark 2: "))
m3 = int(input("Enter Students Mark 3: "))
m4 = int(input("Enter Students Mark 4: "))
m5 = int(input("Enter Students Mark 5: "))
m6 = int(input("Enter Students Mark 6: "))

studentsMark = [1,2,3,4,5,6]
studentsMark.sort()
print(studentsMark)