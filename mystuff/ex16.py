# pulls in sys module and imports argv
from sys import argv
# imports time (function or variable? it is a variable below)
import time

# defines how many arguments argv needs
script, filename = argv

# ourputs f-string with 1 python var input in CLI via argv
print(f"We're going to erase {filename}.")
# outputs text string
print(f"If you won't want that, hit CTRL-C (^C).")
# outputs text string
print("If you do want that, hit RETURN.")

# propts for user input
input("?")

# outputs text string
print("Opening the file...")
# sets var = to open argv file name with status truncated and ready to write
target = open(filename, 'w')
# adds a 3 second pause before next line of code runs
time.sleep(1) # found online and makes this look/feel more real with the pause
# outputs text string
print("Truncating the file. Goodbye!")
# deletes contents inside filename (which was set to 'target' above)
# target.truncate()
# adds a 3 second pause before next line of code runs
time.sleep(1)
# outputs text string
print("Now I'm going to ask you for three lines.")
# sets var = to user input after str prompt
line1 = input("line 1: ")
# sets var = to user input after str prompt
line2 = input("line 2: ")
# sets var = to user input after str prompt
line3 = input("line 3: ")

# debug check on outputs
print(">>>> checking ",repr(line1 + line2 + line3))

# outputs str
print("I'm going to write these to the file.")

# booked asked me to truncate it instead of all the repitition. got error
# when i did the comma's saying (write takes 1 arg, i had six) so i tried +
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
# write (insert into file) whatever line1 var is into line of file
#target.write(line1)
# move onto new line in file
#target.write("\n")
# write (insert into file) whatever line1 var is into line of file
#target.write(line2)
# move onto new line in file
#target.write("\n")
# write (insert into file) whatever line1 var is into line of file
#target.write(line3)
# move onto new line in file
#target.write("\n")
time.sleep(2)

# outputs text string
print("And finally, we close it.")
# closes the text file we were editing (like save->close)
target.close()


# adding study drill portion below. finally worked!!
text = open(filename)
print(text.read())
text.close()
