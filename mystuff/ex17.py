from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

# we could do these two lines on 1 line... how?
# in_file = open(from_file)
# indata = in_file.read()

# answer
indata = open(from_file).read() # answer is correct and CORRECTLY, we get a
# close error becuase you don't need to close, file auto closes at end of line

# debuffing
# print(">>>> the 'indata' var shows", repr(indata))

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
# indata.close()
