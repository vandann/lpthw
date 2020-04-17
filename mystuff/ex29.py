people = 20
cats = 30
dogs = 15

# the if statement decides if the code below it gets to run this time around
if people > cats:
    # code under 'if' statement needs to be indented to operate "inside" the
    # 'if' statement
    print("Too many cat! The world is doomed!")

if people != cats:
    print("Not many cats! The world is saved.")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
