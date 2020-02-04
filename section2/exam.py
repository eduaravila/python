# First, pick a random integer from 1 to 100 using the random module and assign it to a variable
from random import randint

lastAnswer = 0
randomnum = randint(1, 100)

while True:
    userAnwser = int(input("select a number player "))

    if lastAnswer == 0:
        if userAnwser == randomnum:
            print("Got it you win")
            pass
        elif userAnwser < randomnum:
            print("Warm!")
        elif userAnwser > randomnum:
            print("Colder!")
    else:
        if userAnwser == randomnum:
            print("Got it you win")
            pass
        elif userAnwser < randomnum or userAnwser > lastAnswer:
            print("Warmer!")
        elif userAnwser > randomnum or userAnwser < lastAnswer:
            print("Colder!")
    lastAnswer = int(userAnwser)
