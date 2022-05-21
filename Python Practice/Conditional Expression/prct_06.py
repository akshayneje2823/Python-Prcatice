#   WRITE A PROGARAM TO CALCULATE THE GRADE OF A STUDENTS FROM HIS MARKS FROM THE FOLLOWING SCHEME
#         90-100= EX
#         80-90 = A
#         70-90 = B
#         60-70 = C
#         50-60 = D
#         50<   = F

marks = int(input("Enter Your Grade\n: "))

if (marks>=90):
    grade =  "EX"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D"
else:
    grade = "You Are Fail"
print("Your Grade " +grade)