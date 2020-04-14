from sys import argv

script, input_file = argv

def print_line(current_line, f):
    line = int(f.readline())
    print("Zed gave me: ", line, end=' ')
    output = chr(line)
    binary = bin(line)
    print(f"the character is: {output}, which is {binary} in binary")


open_file = open(input_file)

current_line = 1
print_line(current_line, open_file)
# conversion(int(print_line))
current_line += 1
print_line(current_line, open_file)
current_line += 1
print_line(current_line, open_file)
current_line += 1
print_line(current_line, open_file)
current_line += 1
print_line(current_line, open_file)
current_line += 1
print_line(current_line, open_file)
current_line += 1
print_line(current_line, open_file)
current_line += 1
print_line(current_line, open_file)
current_line += 1
print_line(current_line, open_file)
current_line += 1
print_line(current_line, open_file)
current_line += 1
print_line(current_line, open_file)

# print(">>>>open file is:", repr(open_file))

# conversion(input_file)

# input_file.close()
