# room infos:::
# room 1 is frogroom 

import time
from sys import exit

def start():
    print("""You are on a quest to find a powerful crystal on a new planet.
    You have a special backpack with random things that you will need on this quest.
    There are clues you will find along the way to help you find the crystal. The
    planet you are on has very strange creatures and landscapes. Oh, and by the way,
    you need the crystal in order to power your spaceship and get back home\n
    """)
    time.sleep(1)
    room1()

def retry(x):
    choice = input("Do you want to try again? Y/N >")
    if choice == "y" or choice == "Y":
        x()
    else:
        exit(0)

def room1():
    print("You are walking through a jungle when you find an envelope in a bird’s")
    time.sleep(.5)
    print("next. Inside the envelope is a clue to help you find the crystal.")
    time.sleep(.5)
    print("The clue says you need to catch a frog.")
    time.sleep(.5)
    print("You look in your backpack for something to use to catch a frog. What will you use?")
    time.sleep(1)
    print("1. A net")
    print("2. A piece of cheese")
    print("3. A bug catcher")

    choice = input("> ")

    if choice == "1":
        print("It didn’t work! The net got caught on a high tree branch and you are stuck hanging in the air.")
        time.sleep(1)
        retry(room1)
    elif choice == "2":
        print("It worked! The frogs in this jungle like cheese. One came over to you and you were able to catch it.  After the frog ate the cheese it spoke. It said to go find the mountains.")
        time.sleep(1)
        room2()
    elif choice == "3":
        print("It didn’t work. The bug catcher exploded once you took it out of the backpack. Apparently the jungle was too hot for the glass, which caused it to explode.")
        time.sleep(1)
        retry(room1)
    else:
        print("Haha, that wasn't one of the options!")
        time.sleep(1)
        retry(room1)

def room2():
    print("The frog said to find the mountains. You have no idea where the mountains are.")
    time.sleep(1)
    print("How will you find out?")
    time.sleep(1)
    print("1. Climb a high tree and look around")
    print("2. Walk out of the jungle")
    print("3. Ask a magic mirror")

    choice = input("> ")

    if choice == 1:

    elif choice == 2:

    elif choice == 3:

    else:
        print("Haha, that wasn't one of the options!")
        time.sleep(1)
        retry(room2)

def room3():


    choice = input("> ")

    if choice == 1:

    elif choice == 2:

    elif choice == 3:

    else:
        print("Haha, that wasn't one of the options!")
        time.sleep(1)
        retry(room3)

def room4():


    choice = input("> ")

    if choice == 1:

    elif choice == 2:

    elif choice == 3:

    else:
        print("Haha, that wasn't one of the options!")
        time.sleep(1)
        retry(room4)

def room5():


    choice = input("> ")

    if choice == 1:

    elif choice == 2:

    elif choice == 3:

    else:
        print("Haha, that wasn't one of the options!")
        time.sleep(1)
        retry(room5)

def room6():


    choice = input("> ")

    if choice == 1:

    elif choice == 2:

    elif choice == 3:

    else:
        print("Haha, that wasn't one of the options!")
        time.sleep(1)
        retry(room6)

start()
