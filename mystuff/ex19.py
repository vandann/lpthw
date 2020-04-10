import time

# function header (can tell by it started with def), has 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# outputs f-string with 1 python variable, cheese_count (not yet given a value)
    print(f"You have {cheese_count} cheeses!")
# outputs f-string with 1 python var, boxes_of_crackers (not yet give a value)
# note the two variables will need values before function is called
    print(f"You have {boxes_of_crackers} boxes of crackers!")
# outputs text string
    print("Man that's enough for a party!")
# outputs text string and moves cursor to a new line
    print("Get a blanket.\n")
# function ends here as next line is 'de-dented'

# outputs text srt
print("We can just give the function numbers directly:")
# calls function with the 2 numbers as arguments
cheese_and_crackers(20, 30)

# outputs text str
print("OR, we can use variables from our script:")
# sets var = 10
amount_of_cheese = 10
# sets var = 50
amount_of_crackers = 50

# calls function and sets arguments = to the 2 previously defined variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# outputs text str
print("We can even do math inside too:")
# calls function and sets argumetns to value of math in respective comma space
cheese_and_crackers(10 + 20, 5 + 6)

# outputs text str
print("And we can combine the two, variables and math:")
# calls function and sets arguments = value of math in each comma space
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# STUDY DRILL
# function of my own design

def fastcar(horsepower, car_weight, top_speed):
    # below is helpful for debugging and id'ing fn output and when fn ends
    print(">>>> horsepower: ", horsepower, "car weight: ", car_weight, "top speed: ", top_speed)
    print("At this shop we figure out how fast your car is.")
    print(f"Your engine's horsepower is {horsepower} watts.")
    print(f"Your car's total weight is approximately {car_weight} pounds.")
    print(f"And the top speed this car was able to manage was {top_speed}.")
    print(f"Given your hp/tonn is ", round(horsepower / (car_weight/2000), 2), "you have a fast car")
    print("<<<<< exit function here\n")

fastcar(400, 4000, 200)
fastcar(200 * 2, 2000 * 2, 100 * 2)

hp = 400
cw = 4000
ts = 200
fastcar(hp, cw, ts)
fastcar(hp / 1, cw / 1, ts / 1)

hp2 = int(input("car's hp: "))
cw2 = int(input("car's weight: "))
ts2 = int(input("car's top speed: "))
fastcar(hp2, cw2, ts2)


hp3 = int(input("car's hp: "))
cw3 = int(input("car's weight: "))
ts3 = int(input("car's top speed: "))
time.sleep(3)
print("Ahh, I think you're exagerating the horsepower a little.")
fastcar(hp3 * 0.8, cw3, ts3)

fastcar(hp, hp * 10, hp / 2)

fastcar(hp2 + hp3, cw2 + cw3, ts2 + ts3)
