def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# a puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")

what = multiply(age, add(height, subtract(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

# STUDY DRILL formula (5*10-50+100)/2

what2 = divide(add(100, subtract(multiply(5, 10), 50)), 2)
print(what2) #correct

# STUDY DRILL 2 formula with user inputs
print("We are going to add then multiply then we'll subtract and divide. You pick the numbers.")

what3 = divide(
            subtract(
                multiply(
                    add(
                    int(input("first number: ")), int(input("Number you're adding to it: ")))
                , int(input("Number you're multiplying by: ")))
            , int(input("Number you're subtracting: ")))
        , int(input("Number you're dividing by: ")))

print("Hurray!! It worked!! the answer is: ", int(what3))
