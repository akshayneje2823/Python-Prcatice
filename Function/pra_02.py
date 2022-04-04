# WRITE A PYTHON PROGRAM USING FUNCTUON TO CONVERT CELSIUS TO FAHREENITIE

def farh(cel):
    return (cel * (9/5)) + 32 

c = 40
f = farh(c)
print("Fahreheit Temperature is " + str(f))
