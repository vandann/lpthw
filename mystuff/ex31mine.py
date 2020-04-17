import time
# my new game 'find the key and escape'
# lets map the rooms
# electronic collar
# 1 ouside a house (enter widow, basement door, backdoor)
# 2 kitchen (fridge, pantry, random door)
# 3 fridge food (tuna w/ mayo, veggies, steak)
# 4 enjoyed food walk to living room (sit on couch, walk up stairs, lay on floor)
# 5 upstairs 'hear creaking', (open door 1, 2, 3)
# 6 baby's bedroom (creaking is an old mobile)
    # closet, nothing return to search, changing table same, under crib!! yay
# 7 loud noises downstairs, hide in closet, move to another room, climb out window
# 8 on roof undoo collar, climb to other side and down porch, slide down drain, jump
# 9 on ground, sneak silently, mad dash, try and start a car
# snuck to freedom


print("""You wake up for the 12th day out side in the dirt. There is a large
electromagnetic collar around your neck. The only thing you remember from yesterday
is that the kidnappers were making a joke about hiding and a baby. You realize
you need to find the key you ever want to escape this place and see home again.\n""")

print("The kidnappers have just left to run errands and you want to get into the house.")
print("Do you?")
print("1. Attempt to sneak in a side window.")
print("2. Attempt to sneak in the basement door.")
print("3. Attempt to sneak in the back door.")

room1 = input("> ")

if room1 == "1":
    print("You crack the windown and the house alarm goes off.")
    print("When the kidnappers get home they realize what you did.. ded")
elif room1 == "2":
    print("You trip down the basement stairs and break your neck.. ded")
elif room1 == "3":
    print("The back door was left unlocked! You slip inside.\n\n")
    print("Now you're in the kitchen. You look around.")
    print("There's a fridge, a pantry, and a random door, which do you open?")
    print("1. The fridge.")
    print("2. The pantry.")
    print("3. The random door.")

    room2 = input("> ")

    if room2 == "1":
        print("You're actually starving!! and decide to grab some food.")
        print("What to you grab to eat?")
        print("1. Tuna and Mayo")
        print("2. Veggies")
        print("3. Steak")

        room3 = input("> ")

        if room3 == "1":
            print("You take a heaping spoonful of the tuna & Mayo and instantly")
            print("realize it's well past it's expiration and ladened with bacteria.. ded")
        elif room3 == "2":
            print("Veggies, who picks just veggies??? Turs out they aren't the")
            print("edible kinda plants.. ded")
        elif room3 == "3":
            print("You take a couple bites of the steak... Delicious!!")
            print("After finishing the steak you wander towards the front of the house.")
            print("You find yourself in the living room.\n\n")
            print("What do you do?")
            print("1. Sit on the couch.")
            print("2. Walk up the stairs.")
            print("3. Lay on the carpet.")

            room4 = input("> ")

            if room4 == "1":
                print("You end up falling asleep on the couch. The kidnappers ")
                print("find you there when they return.. ded")
            elif room4 == "2":
                print("You turn and start to walk up the stairs.")
                print("Partially up the strairs you hear this creaking..")
                print("Is somebody home? Should I retreat?")
                print("You muster the courage and move up the stairs.\n\n")
                print("You see 3 doors, which do you take?")
                print("1. The closest, door 1.")
                print("2. The partially down the hall, door 2.")
                print("3. The door all the way down the hall, door 3.")

                room5 = input("> ")

                if room5 == "1":
                    print("You open the first door and a bogeyman jumps out and gets you.. ded.")
                elif room5 == "2":
                    print("You open the second door and to your surprise... it's not a door!")
                    print("You fall down the booby trap chute and break your legs in the basement.")
                    print("The kidnappers come home and find you there.. ded.")
                elif room5 == "3":
                    print("The creaking gets louder as you approach the door.")
                    print("You slowly open the door and see it's an infant's bedroom.")
                    print("The creaking was just a spinning mobile above the crib.\n\n")
                    print("What do you do next?")
                    print("1. Search for the key under the crib.")
                    print("2. Search for the key in the closet.")
                    print("3. Search for the key in the changing table.")

                    room6 = input("> ")

                    if room6 == "1":
                        print("Yess!! You find an electromagnetic key under the crib!")
                        print("All of a sudden, you hear noises coming from downstairs!")
                        print("You realize you time is up and the kidnappers are home!\n\n")
                        print("What do you do??")
                        print("1. Hide in the closet.")
                        print("2. Move to another room.")
                        print("3. Climb out the window.")

                        room7 = input("> ")

                        if room7 == "1":
                            print("You slip into the closet and ")
                            print("CRACK! A bear trap clamps on your foot and you pass out.")
                            print("The kidnappers come home and find you there.. ded.")
                        elif room7 == "2":
                            print("You quickly walk out of the room and down the hall.")
                            print("A kidnapper sees you as they are coming up the stairs.. ded.")
                        elif room7 == "3":
                            print("You lock the bedroom door, and climb out the window.")
                            print("the door should hold for a second.. You press")
                            print("the magnetic key to your collar and hear a 'click'.")
                            print("The collar unlocks and falls off with a thud!\n\n")
                            print("Where do you go now?")
                            print("1. Climb to the other side of the roof and then down the porch.")
                            print("2. Slide down the drain spout.")
                            print("3. Jump!")

                            room8 = input("> ")

                            if room8 == "1":
                                print("You climb up and down the peak of the roof onto the porch awning.")
                                print("You then slide down one of the colums onto the porch and")
                                print("then hop down to the ground.\n\n")
                                print("Time is precious, what do you do next?")
                                print("1. Make a mad dash for freedom.")
                                print("2. Sneak silently from bush to bush to the woods.")
                                print("3. Move quickly over to their car to try and start it.")

                                room9 = input("> ")

                                if room9 == "1":
                                    print("The kidnappers immediately see you running across the yard.")
                                    print("They are easily able to run you down.. ded.")
                                elif room9 == "2":
                                    print("You stealthily sneak off their property and to freedom!")
                                    print("Congratulations!! You have survived and escaped!")
                                elif room9 == "3":
                                    print("The kidnappers see you trying to frantically get in the locked car")
                                    print("So close.. but ded.")
                                else:
                                    print("You fail room 9.")


                            elif room8 == "2":
                                print("You grab onto the drainspout to slide down only to have it rip right off the house.")
                                print("You're 30 feet up.. as you fall you realize you really")
                                print("didn't think this one through.. ded.")
                            elif room8 == "3":
                                print("You're 30 feet up.. as you fall you realize you really")
                                print("didn't think this one through.. ded.")
                            else:
                                print("You fail room 8")

                        else:
                            print("You fail room 7.")


                    elif room6 == "2":
                        print("You open the closet door but can't see anything.")
                        print("It must be a deep closet. So you step in")
                        print("CRACK! A bear trap clamps on your foot and you pass out.")
                        print("The kidnappers come home and find you there.. ded.")

                    elif room6 == "3":
                        print("You open the cabinet doors of the changing station")
                        print("and see a little red light flashing... a silent alarm!")
                        print("The kidnappers rush home and find you there.. ded.")

                    else:
                        print("Fail room 6")
                else:
                    print("Fail room 5")

            elif room4 == "3":
                print("You end up falling asleep on the floor. The kidnappers ")
                print("find you there when they return.. ded")
            else:
                print("Fail room 4")

        else:
            print("You fail room 3.")

    elif room2 == "2":
        print("Large food cans and sharp kitchen utensils fall out of the closet!")
        print("You try to leap back, but your magnetic collar attracts those")
        print("sharp kitchen utensils and they skewer you.. ded")
    elif room2 == "3":
        print("Turns out there's a huge hole behind the door and you fall in.. ded")
    else:
        print("You fail room 2.")

else:
    print("You fail room 1.")
