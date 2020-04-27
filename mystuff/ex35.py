# new room, pig_room for study drill

from sys import exit
# I notice here there's no arguments passed to this function... so i guess it
# just runs and doesn't need any inputs
def gold_room():
    print("This room is full of gold. How much do you take?")
    # var below exists only inside gold_room fn unless it's returned out
    choice = input("> ")
    # what this does: or statment and if either are true, we get an int calc
    # if not true the else is portion is run...
    # kinda sux tho cuz it's only 0 or 1 that pulls the numbers
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        # seems to me that I should write the dead function before doing this stuff
        # I wonder if there is an order to writing this that makes sense
        dead("Man, learn to type a number.")
    # new if statment inside gold room (note it is not nexted but comes after)
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        # what is exit, looks like it works just like in the cli the zero is error code
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear in here.")
    print("Ther bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    # variable assigned boolean value
    bear_moved = False
    print(">>> value checking bear_moved", repr(bear_moved)) # dubugging
    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you and then slaps your face off.")
        # this is really cool.. so if string is true and NOT (false) bear_moved
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            # changes boolean variable to True
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room

def pig_room():
    print("You walk in and are greeted with a stench.")
    print("The room is full of pigs and mud.")
    print("Do you walk strait through the room to the door or sneak along the walls?")

    choice = input("> ")

    if "sneak" in choice:
        print("Great job! You didn't fall into the mud pit")
        print("You make it to the door and go inside.")
        bear_room()
    elif "walk" or "strait" in choice:
        dead("You fall into a huge mud pit and sink to the bottom.")
    else:
        print("That isn't a valid choice.")


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        pig_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
