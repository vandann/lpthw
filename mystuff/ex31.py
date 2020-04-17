print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("what do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input ("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    print("4. Close your eyes.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    elif insanity == "4":
        print("Your mind calms and you feel around for anything on the floor.")
        print("You feel a flashlight!")
        print("Do you? ")
        print("1. Shine it into Cthulhu's eye.")
        print("2. Throw it with all your might at Cthulhu's eye.")

        flashlight = input("> ")

        if flashlight == "1":
            print("The eye blasts you with light waves and you melt.")
            print("Good job!")
        elif flashlight == "2":
            print("""Your throwing arm isn't as good as you hoped and the
flashlight plunks on the ground infront of you...""")
            print("Embarassing!")
            print("""Cthulhu's eye, sensing malice, blasts you with light waves
and you melt! Good job!""")
        else:
            print("The insanity rots your eyes into a pool of muck.")
            print("EXTRA Good job!")

    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
