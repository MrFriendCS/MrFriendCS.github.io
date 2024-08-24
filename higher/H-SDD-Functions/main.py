def letterTypes(text):
    "Counts the number of uppercase and lowercase charcters in a string."
    ascii = 0
    uppercase = 0
    lowercase = 0

    for letter in text:

        ascii = ord(letter)

        if ascii >= 65 and ascii <= 90:
            uppercase = uppercase + 1
        elif ascii >= 97 and ascii <= 122:
            lowercase = lowercase + 1

    return uppercase, lowercase


print(letterTypes("Ada Lovelace was the first programmer!"))
print(letterTypes("####! ####!"))
