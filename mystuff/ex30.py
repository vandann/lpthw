people = 40
cars = 0
trucks = 40


if cars > people or trucks > people:
    print("We should take the the vehicles.")
# elif seems to be else/if, like another if statement rolling off the above if
# with there being another else below it at some point to catch when neither of
# the if statments are true
# if there are less cars than people and there are less cars than trucks
elif cars < people and trucks < people:
    print("We can't take just one of the vehicles.")
# if cars and trucks together are > num people and sum of cars and trucks is
# not greater than 2x the number of people
elif cars + trucks > people and cars + trucks <= people * 2:
    print("Hey, we have enough cars & trucks combined! Lets split up the rides.")
else:
    # worked backwards to try and find combo that printed below
    # turns out cars = people and trucks = 0 works or vice versa
    print("We can't decide.")

# this stuff was commented out while i was playing with the above logic statements
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we should take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
