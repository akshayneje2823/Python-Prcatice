import random
myNum = random.randint(0,100)
print("Guess The Number")

while True:
    userNum = int(input("Enter Your Guess: "))

    if(myNum == userNum):
        print("you Won")
        break
    elif myNum > userNum:
        print("Too Low")
    else:
        print("Too High")


