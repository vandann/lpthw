# age var is value user types when prompted by input's question
age = int(input("How old are you? "))
# height var assigned the value user types when prompted by input's question
# added in the age variable as it was defined ABOVE!!!!
height = int(input(f"You're {age}? Nice! How tall are you? "))
# weight var set to value user types when prompted by input question
weight = input("How much do you weigh? ")
# outpouts f-string with 3 python arguments in it.
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
# outputs the string 'age' & string 'height' (they aren't integers)
print(age + height)

# just random test with the blank input
print("how old are youuuu???" , input())
# tried the above per study drills and it's interesting it has input on blank
# line and then outputs it with the print line after something is typed
