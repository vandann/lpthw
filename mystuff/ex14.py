# importing argv from sys modulus
from sys import argv

# setting argv arguments to be written in cli
script, user_name, OS = argv
# var different_prompt = text string
different_prompt = f'{user_name} says: > '
# dubugging
print(">>>> argv=", repr(argv))

# output f-string with 2 python vars (input at cli)
print(f"Hi {user_name}, I'm the {script} script running on {OS}.")
# rewritting with new format.... didn't work
# print("Hi {user_name}, I'm the {script} script.".format(user_name, script))

# output string
print("I'd like to as you a few questions.")
# output f-string with 1 python var from cli
print(f"Do you like me {user_name}?")
# sets var = to user input
likes = input(different_prompt + f'for realz ')
#debugging
print(">>>> likes var got set as:", likes)

# outputs f-string with1 python var from cli
print(f"Where do you live {user_name}?")
# sets var = to user input
lives = input(different_prompt)

print(f"how old are you {user_name}? ")
age = input(different_prompt)

# outputs string
print(f"You're {int(age)}.. What kind of computer do you have?")
# sets var = to user input
computer = input(different_prompt)
print(f"Nice! You're running {OS} on your {computer}... very rad.")

print(">>>> likes var pre output is:", likes)
# outputs block of text with vars that were saved via user's input
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer running {OS}.  Nice.
""")
