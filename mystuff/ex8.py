# sets var formatter with 4 open arguments
formatter = "{} {} {} {}"

# output formatter var with format (f-string) vals 1,2,3,4
# tested and it didn't print the 5th nor did it throw an error
print(formatter.format(1 + 1, 2, 3, 4, 5))
# ourput formatter var with format (f-string) vals written as strings
print(formatter.format("one", "two", "three", "four"))
# output formatter var with format (f-string) vals written as bools
print(formatter.format(True, False, False, True))
# output formatter var with format (f-string) vals written as it's own variable
# thus outputting the string that 'formatter' is set = to
print(formatter.format(formatter, formatter, formatter, formatter))
# output formatter var with format (f-string) vals as strings below
# note the fifth line below was not output.. remove comma and it is
print(formatter.format(
    "Bring me a higher love",
    "Briiiiiinnnng me a higher love",
    "That's what I'm calling",
    "A higher love.",
    "Bring... meee.... a higher love."
))
