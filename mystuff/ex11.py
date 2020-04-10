# outputs question and keeps line
print("How old are you?", end=' ')
# awaits user input and assigns it to var age
age = input()
# outputs question and keeps line
print("How tall are you?", end=' ')
# awaits user input and assigns it to var height
height = input()
# outputs question and keeps line
print("How much do you weight?", end=' ')
# awaits user input and assigns it to var weight
weight = input()

# outputs f-string with 3 pythons arguments from previous user inputs
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# tried another version and it worked!
age = int(input("How old are you?")) # went over int function to make input a #
height = input("How tall are you?")
weight = input("How much do you weight?")

# study drill 3 "write another form"

print("\n\n\n\nUnemployment Application", end=' ')
input()
name = input('\n\nwhat is your full name? ')
last_day = input('what day was your last date of employment? ')
prev_employer = input('how long were you at your previous employer? ')
paycheck = input('what was your weekly paycheck? ')
availability = input('when are you able to join the workforce? ' )
able_body = input('Are you able to lift objects over 20lbs? ')

input('\n\n\npress \'enter\' to process.')


print('\n\nplease verify the infomation you provided below.\n')
print(f'Your full name is {name}.')
print(f'Your last date of employment was {last_day}.')
print(f'You previously worked for {prev_employer}.')
print(f'Your previous paychecks amounted to {paycheck} weekly.')
print(f'You are available to join the workfore on {availability} date.')
print(f'You said {able_body} to lifting objects over 20lbs.')

input('\npress \'enter\' to verify answers are correct.')
