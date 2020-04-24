# thought about a fibonacci program while on a walk today and how i could
# use a loop to run it
# for reference to other examples of the loops see ex33

import time

fibs = ['0', '1']
n = 1
f = 0

print(f)
print(n)

for x in range(10):
    f = n + f
    print(f)
    # time.sleep(1)
    fibs.append(str(f))
    n = f + n
    print(n)
    # time.sleep(1)
    fibs.append(str(n))

print(fibs)
