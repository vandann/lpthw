list = [1, 2, 3, 4]

print("the original list:" + str(list))

# extend function

list.extend(range(6, 11, 2))

print("new list:" + str(list))

list2 = ['this', 'that', 'another']

# no str() gave me a tuple error (is tuple the default??)
print("original list2:" + str(list2))

list2a = ['something', 'another thing', 'last thing']

# extend worked nicely.. trying append now
list2.append(list2a)

print("new list2:" + str(list2))
print("now print emd strait")
print(list2)
print(list2a)
# list2b = list2 + list2a

# print("OR make them a new var:" + str(list2b))
