name = 'Dan vanDann'
age = 33 # not a lie
height = 74.0 # inches
height_in_cm = round(height * 2.54)
weight = 180 # lbs
weight_in_kg = round(weight / 2.20)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")
print(f"If you want to know my height in centimeters, it is {height_in_cm}.")
print(f"If you want to know my weight in kilograms, it is {weight_in_kg}.")
# this line is tricky, try to get it exactly right
total = int(age + height + weight)
print(f"If I add {age}, {height}, and {weight} I get {total}.")
