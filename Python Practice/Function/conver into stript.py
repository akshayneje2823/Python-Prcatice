# write a python function to remove a given word from a string and strim it at the same time

nikal = "   Harry is good   "
def remove_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

n = remove_split(nikal, "Harry")
print(n)