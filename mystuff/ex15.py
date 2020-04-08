# imports argv from sys module
from sys import argv

# gives number and name of argv "index?" arguments
script, filename = argv

# sets var txt = to
txt = open(filename)
print(">>>> ", repr(txt))# curious what it shows

# outputs f-string with 1 python var from argv input
print(f"Here's your file {filename}:")
# outputs txt var with funtion read() run on it
print(txt.read())

# output string
print("Type the filename again:")
# set var = to user input after >
file_again = input("> ")
# tested diff method
# file_again = input(f"Type the filename, {filename}, again: > ")

# sets var = to open funciton on user input file_again var
txt_again = open(file_again)
# outputs txt_again var with funtion read() on it
print(txt_again.read())
txt.close()
txt_again.close()
