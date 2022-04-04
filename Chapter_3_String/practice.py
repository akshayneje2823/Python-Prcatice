#Write a python prpgram to display a user entered name followed by good afternoon using input function

name = input("Enter your name\n")
print("Good Afternoon," + name)

#Write a program to fill in a letter template given by below with name and date 
  #letter = '''Dear <name>
                  #You are swlwcted!
                  #<Date>'''

letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell about your selection
You are selected!
Have a grate day ahed!
Thanks and regar
Dare: <|DATE|>
'''
name = input("Enter our Name\n")
date = input("Enter Date\n")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)

#Q-3 WRITE A PROGRAM TO DETECT DUBBLE SPACES IN A STRING

st = "This is a string with double  spaces"
doublespace = st.find("  ")
print(doublespace)


# Q-4 Q3 replace with single spaces
st = st.replace("  ","  ")
print(st)

# Q-5 WRITE A PROGRAM TO FPRMAT THE FOLLOWING LETTERS USING ESCAPE SEQUENCES CHARATERS

letter = "Dear harry,\nThis is a paython program! Thanks!"
print(letter)
ans = "Dear harry,\n\tThis is a paython program!\n Thanks!"
print(ans)


