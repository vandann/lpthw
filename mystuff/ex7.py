# outputs text in quotes
print("Mary had a little lamb.")
# outputs text in quotes has python brace that would be empty except for the
# format with argumement snow (f-string)
print("Its fleece was white as {}.".format('snow'))
# trying anothe version of the above
poem_line_2 = "Its FLEECE was white as {}."
snow2 = 'snow'
print(poem_line_2.format(snow2)) # YAY, it worked!

# outputs text in quotes
print("And everwhere that Mary went.")
# outputs a . 10 times
print("." * 10) # what'd that do?
# answer it made 10 periods so it did "." 10 times

# var end1 is now C
end1 = "C"
# var end2 is now h
end2 = "h"
# var end3 is now e
end3 = "e"
# var end4 is now e
end4 = "e"
# var end5 is now s
end5 = "s"
# var end6 is now e
end6 = "e"
# var end7 is now B
end7 = "B"
# var end8 is now u
end8 = "u"
# var end9 is now r
end9 = "r"
# var end10 is now g
end10 = "g"
# var end11 is now e
end11 = "e"
# var end12 is now r
end12 = "r"

# watch end ' ' at the end.  try removing it and see what happens
# output var end1 -> add on the var end2 -> add on var end3 etc etc
# I DON'T QUITE KNOW WHAT THE 'end= ' '' means
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# output var end7 -> add on var end8 etc etc
print(end7 + end8 + end9 + end10 + end11 + end12)
