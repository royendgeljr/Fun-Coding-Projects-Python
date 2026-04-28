import random

randomnumber = random.randrange(1,10)
number = input("Guess the Number!")
number = int(number)

if number != randomnumber:
    print("nope, it's ", randomnumber, ". your answer: ", number)
else:
    print("success! You got it, it was indeed", number)