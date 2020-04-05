types_of_people = 10 # sets var to 10
x = f"There are {types_of_people} types of people."
# sets var x to f-string w/ a python variable in braces

binary = "binary" # sets var
do_not = "don't" # sets var
y = f"Those who know {binary} and those who {do_not}."
# sets var y to f-string w/ 2 python variables in braces


print(x) # output variable x
print(y) # output variable y

print(f"I said: {x}") # output f-string with a python variable x
print(f"I also said: '{y}'")  # output f-string with a python variable y

hilarious = False # sets var with boolean value False
joke_evaluation = "Isn't that joke so funny?! {}"
# sets variable with empty python braces????

print(joke_evaluation.format(hilarious)) # output var joke_evaluation formatted
# string adds python and value hilarious(var) is then populated in empty brace

# played with one other modification
print(joke_evaluation.format(y), "get it?")

# trying another verious of above to see if it works
print(f"{joke_evaluation}{hilarious}") #this doesn't take care of the input
# inside the joke_evaluation variable

w = "This is the left side of..." # sets var with string value
e = "a string with a right side." # sets var with string value

print(w + e) # output string w and put string e on the end
