# the game rock paper scissor
#user input
# then random gen by computer
# then winner selected
# then do you want to play again "if yes return function name"

import time
import random

again = "yes"

print("Let's play 'Rock Paper Scissor'!!")

def main(again):
    print("Round 1: what do you pick")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    # person = 1
    user = input("> ")
    # print(">>>> value of user", repr(user))
    if user == "1":
        person = "Rock"

    elif user == "2":
        person = "Paper"

    elif user == "3":
        person = "Scissor"

    else:
        print("error")

    print(f"Ok, {person}.")
    time.sleep(1)

    computer = random.randint(1,3)
    # print(">>>> value of computer", repr(computer))
    if computer == 1:
        rand = "Rock"
    elif computer == 2:
        rand = "Paper"
    elif computer == 3:
        rand = "Scissor"
    else:
        print("Somethings wrong... check compter randint function")

    print("Here we go.")
    time.sleep(1)
    print("Rock...")
    time.sleep(1)
    print("Paper...")
    time.sleep(1)
    print("Scissor...")
    time.sleep(1)
    print("Shoot!")
    time.sleep(1)

    print("You rolled {} and the computer rolled {}.".format(person,rand))

    if person == rand:
        print("You tied!!")
    elif person == "Rock" and rand == "Paper":
        print("The computer wins! Boo!")
    elif person == "Rock" and rand == "Scissor":
        print("You win! Hurray!")
    elif person == "Paper" and rand == "Rock":
        print("You win! Hurray!")
    elif person == "Paper" and rand == "Scissor":
        print("The computer wins! Boo!")
    elif person == "Scissor" and rand == "Rock":
        print("The computer wins! Boo!")
    elif person == "Scissor" and rand == "Paper":
        print("You win! Hurray!")
    else:
        print("This is another error, check winning logic")

    time.sleep(1)

    again = input("Do you want to play agin?> ")

    if again == "yes" or again == "Yes" or again == "y" or again == "Y":
        return main(again)
    else:
        print("Oh kay, byeeeeeee....")
main(again)
