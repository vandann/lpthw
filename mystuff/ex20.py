# pull from sys modulus and import argv
from sys import argv

# unpacks argv with 2 arguments
script, input_file = argv

# starts function with one argument called f
def print_all(f):
# outputs, "read whatever f is (all of it)"
    # print(">>>> print_all: f=", repr(f))
    print(f.read())
    # print("<<<<< print_all: f=", repr(f))

# starts function with one argument called f
def rewind(f):
# runs function to find character "0" a.k.a "rewind to the start"
    # print(">>>> rewind: f=", repr(f))
    f.seek(0)
    # print("<<<< rewind: f=", repr(f))

# starts function with 2 args, line_count and f
def print_a_line(line_count, f):
# outputs var line_count and has function read the line in "f"
    # print(">>>> print_a_line: f=", repr(f))
    print(line_count, f.readline())#, end = "")
    # print("<<<< print_a_line: f=", repr(f))
# sets var = opening whatever file input_file is
current_file = open(input_file)

# outputs text str with new line after
print("First let's print the whole file:\n")

# calls function 'print_all' and executes it on now defined var, current_file
print_all(current_file)
#outputs text str
print("Now let's rewind, kind of like a tape.")

# calls function 'rewind' and executes it on the variable "current_file"
rewind(current_file)
# TESTED what happens if you remove rewind!
# turns out it functions like a tape deck, it isn't able to output the lines as
# the computer appears to only 'seek' forward.

# outputs text str
print("Let's print three lines:")

# sets var to 1
current_line = 1
# calls function "print_a_line" and outputs current_line var (1) and
# current_file which is still = to open(input_file)
print_a_line(current_line, current_file)
# sets var to 2 (n+1)
current_line += 1
# calls function "print_a_line" and outputs current_line var (now 2) and
# current_file which is still = to open(input_file)
print_a_line(current_line, current_file)

# sets var to 3 (n+1)
current_line += 1
# calls function "print_a_line" and outputs current_line var (now 2) and
# current_file which is still = to open(input_file)
print_a_line(current_line, current_file)
