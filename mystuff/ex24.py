print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requres an explanation
\n\t\twhere there is none.
"""

print("------------")
print(poem)
print("------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# method secret_formula and it takes one input
def secret_formula(started):
    # sets variable value = to function's input * 500
    jelly_beans = started * 500
    # var is = to above var and math
    jars = jelly_beans / 1000
    # var is = to above var and math
    crates = jars / 100
    # send out of the function the 3 variable values that were created here
    return jelly_beans, jars, crates

# setting random variable value,
start_point = 10000

# my guess is since fn 'secret_formula' returns 3 variables, you can/need to set
# the outputs equal to variables outside the function if you want to use the values
# somewhere without calling the fn
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with the f-string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")
print(">>>> start_point value before calc", repr(start_point))
start_point = start_point / 10
print(">>>> start_point value after calc ", repr(start_point))
print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print(">>>> formula value ", repr(formula))
# I don't think you can f-string this since formula contains multiple values
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
