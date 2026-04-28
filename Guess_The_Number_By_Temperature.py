import time
import random

print("Welcome to Guess the Number by Temperature!")
time.sleep(1)

for i in range(0,3):
    print(".")
    time.sleep(.5)
    
time.sleep(.5)

table = [
    10,
    100,
    1000,
    10000
    ]

game = ["0. solo",
        "1. vs_robot",
        "2. introduction"
        ]

robotfailures = ["Nooo! let me try again.",
                "I'm gonna get it right this time!",
                "Bruhhh.",
                "Really?",
                "This is annoying.",
                "I'm gonna get it.",
                "I will show you who I am!",
                "Oh my days.",
                "I'm winning any ways.",
                "You're losing any ways.",
                "Ugh!",
                "Ugh.",
                "Well!",
                "This is fun..",
                "Give up."
]

robotsuccesses = ["YES!!!",
                "I got it right!",
                "Oh yeahh!",
                "Just like that.",
                "This is joyful!",
                "I got it!",
                "That's who I am!",
                "Let's Go!!!",
                "I knew I'd win!",
                "I knew you'd lose!",
                "Aha!",
                "Gotcha!",
                "Well, Well, Well, look who has won!",
                "This is actually fun!",
                "Don't give up..!"
]

def robotfailuregenerator():
    global robotfailure
    robotfailure = robotfailures[random.randrange(0,14)]

def robotsuccessgenerator():
    global robotsuccess
    robotsuccess = robotsuccesses[random.randrange(0,14)]


def generator():
    print(table)
    while True:
        chosen_encoded_number = input("Choose numbers 0 to 3 from given table.  ")
        if chosen_encoded_number in ["0","1","2","3"]:
            print("Alright.")
            break
        elif chosen_encoded_number == "":
            print("You can't leave blank!")
        elif chosen_encoded_number not in ["0","1","2","3"]:
            print("You can't type that!")
        
    time.sleep(.5)

    global chosen_number
    chosen_number = table[int(chosen_encoded_number)]
    print("Generating Number...")
    global randomnumber
    randomnumber = random.randrange(1, chosen_number)

    time.sleep(1)

def solo():
    print("Game has begun!")

    tries = 0

    while True:
        while True:
            print("--------------------")
            number = input("Guess the number:   ")
            if number == "":
                print("You can't leave blank!")
                continue
            try:
                number = int(number)
                print("--------------------")
                break
            except ValueError:
                print("You can't type that!")
        if number == randomnumber:
            print("Success!", tries, "tries")
            print("/-/-/-/-/-/-/-/-/-/")
            print("")
            break
        elif number >= randomnumber:
            print("Lower!")
            tries += 1
        elif number <= randomnumber:
            print("Higher!")
            tries += 1

def vsrobot():
    print("Game has begun!")

    robotmode = 0

    while True:
        randomplayernumber = input("What's your secret number??: ")
        if randomplayernumber == "":
            print("You can't leave blank!")
        try:
            randomplayernumber = int(randomplayernumber)
            while True:
                if randomplayernumber >= chosen_number:
                    print("You can't go above the number you've chosen!")
                    randomplayernumber = input("What's your secret number??: ")
                    try:
                        randomplayernumber = int(randomplayernumber)
                    except ValueError:
                        print("You can't type that!")
                elif randomplayernumber <=0:
                    print("You can't go below 1!")
                    randomplayernumber = input("What's your secret number??: ")
                    try:
                        randomplayernumber = int(randomplayernumber)
                    except ValueError:
                        print("You can't type that!")
                else:
                    print("Alright.", randomplayernumber)
                    break
            break
        except ValueError:
            print("You can't type that!")
    
    while True:
        print("['0. Normal', '1. Hard']")
        robotmode = input("Choose robot dificulty:  ")
        if robotmode in ["0","1"]:
            break
        elif robotmode == "":
            print("You can't leave blank!")
        elif robotmode not in ["0","1"]:
            print("You can't type that!")

    tries = 0
    robottries = 0

    firstrobotnumber = 1
    secondrobotnumber = chosen_number

    robottableofdissapointment = []

    while True:
        while True:
            print("--------------------")
            number = input("Guess the number:   ")
            if number == "":
                print("You can't leave blank!")
                continue
            try:
                number = int(number)
                print("--------------------")
                break
            except ValueError:
                print("You can't type that!")
        if number == randomnumber:
            print("Success!", tries, "tries")
            break
        elif number >= randomnumber:
            print("Lower!")
            tries += 1
        elif number <= randomnumber:
            print("Higher!")
            tries += 1

        try:
            if robotmode == "0":
                randomrobotnumber = random.randrange(firstrobotnumber, secondrobotnumber)
                if secondrobotnumber-firstrobotnumber <= 0:
                    print("Whoops!")
                    break
                elif randomrobotnumber in robottableofdissapointment:
                    while randomrobotnumber in robottableofdissapointment:
                        randomrobotnumber = random.randrange(firstrobotnumber, secondrobotnumber)
                        print("                                         Robot: Dissapointment..!")
                        time.sleep(.1)
            elif robotmode == "1":
                randomrobotnumber = (firstrobotnumber+secondrobotnumber) // 2
        except ValueError:
            print("Whoops!")

        if randomrobotnumber == randomplayernumber:
            robotsuccessgenerator()
            print("                                        " "Robot: //", robotsuccess, "//")
            print("                                        Robot: // You lost! I won with", robottries, "tries" " //")
            print("/-/-/-/-/-/-/-/-/-/")
            print("")
            break
        elif randomrobotnumber >= randomplayernumber:
            print("                                         Robot: // Lower..! //")
            robottries += 1
            secondrobotnumber = randomrobotnumber
            robottableofdissapointment.append(randomrobotnumber)
            robotfailuregenerator()

        elif randomrobotnumber <= randomplayernumber:
            print("                                         Robot: // Higher..! //")
            robottries += 1
            firstrobotnumber = randomrobotnumber
            robottableofdissapointment.append(randomrobotnumber)
            robotfailuregenerator()
        print("                                         //", robotfailure, randomrobotnumber, "(",firstrobotnumber, secondrobotnumber,") //")

def introduction():
    print("Guess The Number By Temperature, Introduction!")
    time.sleep(1)
    print("You will first be asked to enter a game mode:")
    print("0 = solo" \
    "1 = vs_robot" \
    "2 = introduction")
    time.sleep(2)
    print("")
    print("                 SOLO")
    print("You will then get prompted to choose a number between 0 and 3:")
    print("0 = range 1 to 10" \
    "1 = range 1 to 100" \
    "2 = range 1 to 1000" \
    "3 = range 1 to 10000")
    time.sleep(2)
    print("The selected range will then get a random number. You don't know it.")
    time.sleep(.5)
    print("After it generates the number, the game begins!")
    time.sleep(.5)
    print("You will then need to guess the number between the range you've chosen.")
    print("if you fail, it will print: 'Higher!' or 'Lower!'.")
    print("Then you will need to guess a lower or a higher number.")
    time.sleep(1)
    print("By the moment you win, you will recieve how many tries you've made.")

    time.sleep(2)

    print("")
    print("                 VS_ROBOT")
    print("You will get asked to choose a number between 0 and 3:")
    print("0 = range 1 to 10" \
    "1 = range 1 to 100" \
    "2 = range 1 to 1000" \
    "3 = range 1 to 10000")
    time.sleep(2)
    print("The selected range will then get a random number. You don't know it.")
    time.sleep(.5)
    print("After it generates the number, the game begins!")
    time.sleep(.5)
    print("You will get prompted to type your secret number.")
    print("This secret number needs to be a value between the range you've chosen.")
    print("The robot will try to guess fair-and-square your number.")
    print("If you win, you will recieve how many tries you've made.")
    time.sleep(.5)
    print("If the robot wins, it will show how many tries the robot made.")
    time.sleep(2)
    print("The chat on the left is yours!")
    time.sleep(.5)
    print("The chat on the right ('Robot: ...') is for the robot!")

while True:
    print(game)
    gamechoice = input("Choose 0, 1 or 2   ")
    if gamechoice == "0":
        print("Alright.")
        generator()
        solo()
    elif gamechoice == "1":
        print("Alright.")
        generator()
        vsrobot()
    elif gamechoice == "2":
        print("Alright.")
        introduction()
    elif gamechoice == "":
        print("You can't leave blank!")
    elif gamechoice not in ["0","1","2"]:
        print("You can't type that!")
