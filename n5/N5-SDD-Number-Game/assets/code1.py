import random
num1 = random.randint(1, 10)
num2 = int(input("What is one bigger than " + str(num1) + "? "))
if num2 == num1 + 1:
    print("Correct - Well done!")
if num2 > num1 + 1:
    print("Too big!")
    print(str(num1 + 1) + " is one bigger than " + str(num1))
if num2 < num1:
    print("Too small!")
    print(str(num1 + 1) + " is one bigger than " + str(num1))
if num2 == num1:
    print("That's the same!")
    print(str(num1 + 1) + " is one bigger than " + str(num1))
