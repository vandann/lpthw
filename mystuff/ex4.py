cars = 100 # var 'cars' given value
space_in_a_car = 4.0 # var 'space_in_a_car' given value
drivers = 30 # var 'drivers' given value
passengers = 90 # var 'passengers' given value
cars_not_driven = cars - drivers # calcs value for 'cars_not_driven'
cars_driven = drivers # sets 'cars_driven' equal to # of drivers
carpool_capacity = cars_driven * space_in_a_car
# calcs value for carpool_capacity
average_passengers_per_car = passengers / cars_driven
# calcs value for average_passengers_per_car


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
