# var set to zero
i = 0
# variable set to empty list
numbers = []

# while loop that runs as long as i is less than 6
while i < 6:
# outputs f-string with the current i variable value
    print(f"At the top i is {i}")
# adds a single argument 'i' to the end of the numbers list
    numbers.append(i)

# also known as i += 1, basically adds one to i
    i = i + 1
# outputs text str and variable numbers (which is a list of values)
    print("Numbers now:", numbers)
# outpouts f-string and the i variable (which has a new value after the above formula)
    print(f"At the bottom i is {i}")

# outputs string
print("The numbers: ")

# starts a for loop with new variable 'num' and runs
# if the value of 'num' is inside the 'numbers' list
for num in numbers:
# outputs the num on the current line
    print(num)



# ran the above with a funciton
i = 0
a = i + 1
numbers = []

def main(i, a):
    print(f"At the top i is {i}")
    numbers.append(i)
    a = i + 1
    i = i + a
    print("Numbers now:", numbers)
    print(f"At the bottom i is {i}")
    if i < 82:
        return main(i, a)
    # hmm i guess I don't need to have an else
    # else:
        # print('program done')

main(i, a)

print("The numbers: ")

for num in numbers:
    print(num)

# running the above with a for loop
i = 0
numbers = []
for i in range(6):
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now:", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
