import time
from sys import exit

def start():
    print("""
    You are on a quest to find a powerful crystal on a new planet.
    You have a special backpack with random things that you will need on this quest.
    There are clues you will find along the way to help you find the crystal. The
    planet you are on has very strange creatures and landscapes. Oh, and by the way,
    you need the crystal in order to power your spaceship and get back home
    """)
    time.sleep(1)
    room1()

def retry(x):
    choice = input("Do you want to try again? Y/N >")
    if choice == "y" or choice == "Y":
        x()
    else:
        exit(0)

def final():
    print("""
    Congratulations! You found the crystal! The moment you touched the crystal
    you were transported back to your ship.  Now you can power your space ship
    and return home!
    """)

# room1 is frog_room
def room1():
    print("You are walking through a jungle when you find an envelope in a bird’s")
    time.sleep(.5)
    print("next. Inside the envelope is a clue to help you find the crystal.")
    time.sleep(.5)
    print("The clue says you need to catch a frog.")
    time.sleep(1)
    print("You look in your backpack for something to use to catch a frog. What will you use?")
    time.sleep(1)
    print("1. A net")
    print("2. A piece of cheese")
    print("3. A bug catcher")

    choice = input("> ")

    if choice == "1":
        print("It didn’t work! The net got caught on a high tree branch and you")
        print("are stuck hanging in the air.")
        time.sleep(1)
        retry(room1)
    elif choice == "2":
        print("It worked! The frogs in this jungle like cheese. One came over ")
        print("to you and you were able to catch it.  After the frog ate the ")
        print("cheese it spoke. It said to go find the mountains.")
        time.sleep(1)
        room2()
    elif choice == "3":
        print("It didn’t work. The bug catcher exploded once you took it out ")
        print("of the backpack. Apparently the jungle was too hot for the glass, ")
        print("which caused it to explode.")
        time.sleep(1)
        retry(room1)
    else:
        print("Haha, that wasn't one of the options!")
        time.sleep(1)
        retry(room1)

# room2 is find_mountain
def room2():
    print("The frog said to find the mountains. You have no idea where the mountains are.")
    time.sleep(1)
    print("How will you find out?")
    time.sleep(1)
    print("1. Climb a high tree and look around")
    print("2. Walk out of the jungle")
    print("3. Ask a magic mirror")

    choice = input("> ")

    if choice == "1":
        print("It didn’t work. You fell out of the tree before you reached the top")
        print("and landed in a large puddle of glue. You are stuck.")
        time.sleep(1)
        retry(room2)
    elif choice == "2":
        print("It didn’t work. You walked out of the jungle and landed in a deep")
        print("pit. You can’t get out.")
        time.sleep(1)
        retry(room2)
    elif choice == "3":
        print("It worked! The mirror said the mountains are south of you.")
        print("It said to put on your rocket pack and fly there.")
        time.sleep(1)
        room3()
    else:
        print("Haha, that wasn't one of the options!")
        time.sleep(1)
        retry(room2)

# room3 is mountain_cave
def room3():
    print("Flying was amazing! You reached the mountains. Now you need to find")
    time.sleep(.5)
    print("where the next clue is. You see a cave and go in. The cave is dark")
    time.sleep(.5)
    print("and damp. You use your flashlight to see where to go. As you shine")
    time.sleep(.5)
    print("it around, you see eyes looking at you.  It turns out to be a large")
    time.sleep(.5)
    print("3 eyed, blue spotted alien with five arms.  He is fast and quickly grabs you.")
    time.sleep(1)
    print("How do you get away from him?")
    time.sleep(1)
    print("1. Kick him in the head.")
    print("2. Use a bat from your backpack and hit him.")
    print("3. Tickle him.")

    choice = input("> ")

    if choice == "1":
        print("It worked! Kicking him made him dizzy and he dropped you.")
        print("Now you run!")
        time.sleep(1)
        room4()
    elif choice == "2":
        print("It didn’t work. He saw you swing and grabbed the bat with a")
        print("free hand. He then broke it. The alien ties your hands up.")
        time.sleep(1)
        retry(room3)
    elif choice == "3":
        print("It didn’t work. Tickling him made him laugh but he still holds you tight.")
        time.sleep(1)
        retry(room3)
    else:
        print("Haha, that wasn't one of the options!")
        time.sleep(1)
        retry(room3)

# room4 is pudding_tunnel
def room4():
    print("As you run, you spot a chest on the cave floor. You grab it, thinking ")
    time.sleep(.5)
    print("it might be the crystal. Once you are outside, you open it. It’s ")
    time.sleep(.5)
    print("another clue. It says to dig a tunnel.  It turns out the ground ")
    time.sleep(.5)
    print("underneath you is actually pudding. ")
    time.sleep(1)
    print("What will you use to dig?")
    time.sleep(1)
    print("1. A spoon")
    print("2. An excavator")
    print("3. Your hands")

    choice = input("> ")

    if choice == "1":
        print("It didn’t work. The pudding tunnel collapsed on top of you.")
        time.sleep(1)
        retry(room4)
    elif choice == "2":
        print("It didn’t work.  The excavator went full throttle and drove off the mountain.")
        time.sleep(1)
        retry(room4)
    elif choice == "3":
        print("It worked! Your hands are sticky but you dug a tunnel under the ")
        print("mountain came out the other side. ")
        time.sleep(1)
        room5()
    else:
        print("Haha, that wasn't one of the options!")
        time.sleep(1)
        retry(room4)


# room5 is crater_crossing
def room5():
    print("On the other side of the mountain you find a large crater. You can’t ")
    time.sleep(.5)
    print("go through it or around it. You must go over it. You peer inside the ")
    time.sleep(.5)
    print("crater and see some strange looking animals with great tickling skills. ")
    time.sleep(.5)
    print("You definitely do not want to fall in. ")
    time.sleep(1)
    print("How will you get across the crater?")
    time.sleep(1)
    print("1. Build a bridge with legos ")
    print("2. Fly across with a hang glider")
    print("3. Ride on an eagle")

    choice = input("> ")

    if choice == "1":
        print("It worked! The bridge held and the animals were not able to")
        print("get you. You found a mailbox on the other side with a clue in it.")
        time.sleep(1)
        room6()
    elif choice == "2":
        print("It didn’t work. The hang glider got a tear in it and you fell")
        print("into the pit. The animals cornered you and started tickling you.")
        time.sleep(1)
        retry(room5)
    elif choice == "3":
        print("It didn’t work. OH NOOOOO!!")
        print("The eagle got distracted as it was flying")
        print("and took you all the way back to the MOUNTAINS.")
        time.sleep(2)
        room3()
    else:
        print("Haha, that wasn't one of the options!")
        time.sleep(1)
        retry(room5)


# room6 is ocean_crossing
def room6():
    print("You read the next clue, which said to go across the ocean to an ")
    time.sleep(.5)
    print("island. When you reach the ocean, you realize that it’s not water, ")
    time.sleep(.5)
    print("it’s bubble solution. The ocean is not water, it’s bubbles. ")
    time.sleep(1)
    print("How will you cross to the island?")
    time.sleep(1)
    print("1. Take a boat")
    print("2. Ride on a bubble wand")
    print("3. Take a surf board")

    choice = input("> ")

    if choice == "1":
        print("It didn’t work. Your boat was too heavy and it sank in the bubble solution.")
        time.sleep(1)
        retry(room6)
    elif choice == "2":
        print("It worked! You made it across to the island.")
        time.sleep(1)
        room7()
    elif choice == "3":
        print("It didn’t work. The surf board got stuck inside a large")
        print("bubble and you are trapped floating around in the sky.")
        time.sleep(1)
        retry(room6)
    else:
        print("Haha, that wasn't one of the options!")
        time.sleep(1)
        retry(room6)


# room7 is island_buildings
def room7():
    print("On the island you used your binoculars and say that there were three ")
    time.sleep(.5)
    print("buildings. You assume that you need to look in one of these buildings ")
    time.sleep(.5)
    print("for the next clue or crystal. ")
    time.sleep(1)
    print("Which building do you decide to go in?")
    time.sleep(1)
    print("1. The house")
    print("2. The bank")
    print("3. The  alien’s fort")

    choice = input("> ")

    if choice == "1":
        print("It didn’t work. The house was an illusion. When you entered")
        print("you were caught up in a net.")
        time.sleep(1)
        retry(room7)
    elif choice == "2":
        print("It didn’t work. When you entered the bank, all the doors")
        print("and windows locked and you couldn’t get out.")
        time.sleep(1)
        retry(room7)
    elif choice == "3":
        print("It worked! You entered the fort and found yourself in a room with a safe.")
        time.sleep(1)
        room8()
    else:
        print("Haha, that wasn't one of the options!")
        time.sleep(1)
        retry(room7)


# room8 is fort_dogs
def room8():
    print("The safe in the room is glowing. You assume the crystal must be in ")
    time.sleep(.5)
    print("there. Unfortunately, there are three alien dogs guarding it. ")
    time.sleep(.5)
    print("If they get close to you, their breath will freeze you like ice. ")
    time.sleep(1)
    print("What will you do to stop the dogs?")
    time.sleep(1)
    print("1. Read them a story that puts them to sleep")
    print("2. Offer them dog food")
    print("3. Lay down and pretend to sleep")

    choice = input("> ")

    if choice == "1":
        print("It worked! The dogs love stories and they fell asleep.")
        time.sleep(1)
        room9()
    elif choice == "2":
        print("It didn’t work. These dogs don’t like dog food. They approached")
        print("you and breathed on your face. Their breath made you freeze like ice.")
        time.sleep(1)
        retry(room8)
    elif choice == "3":
        print("It didn’t work. When you laid down you triggered a pressure plate.")
        print("This caused a cage to come up from the floor and entrap you.")
        time.sleep(1)
        retry(room8)
    else:
        print("Haha, that wasn't one of the options!")
        time.sleep(1)
        retry(room8)


# room9 is unlock_safe
def room9():
    print("Now that the dogs are asleep you can creep quietly around them. ")
    time.sleep(.5)
    print("You feel certain that the crystal is in the safe. You have to figure ")
    time.sleep(.5)
    print("out how to open it with something from your backpack. ")
    time.sleep(1)
    print("What will you use?")
    time.sleep(1)
    print("1. A key")
    print("2. A Pokémon card")
    print("3. An xbox controller ")

    choice = input("> ")

    if choice == "1":
        print("It didn’t work. When you turned the key, a toxic spray came out")
        print("and caused you to fall asleep.")
        time.sleep(1)
        retry(room9)
    elif choice == "2":
        print("It worked! The safe opened and there was the crystal.")
        print("You carefully picked it up.")
        time.sleep(1)
        final()
    elif choice == "3":
        print("It didn’t work. After you pushed X on the controller, slime")
        print("dumped on top of you.")
        time.sleep(1)
        retry(room9)
    else:
        print("Haha, that wasn't one of the options!")
        time.sleep(1)
        retry(room9)

start()
