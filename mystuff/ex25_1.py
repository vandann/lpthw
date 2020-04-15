def breakup(stuff):
    # this breaks apart the sentence into an array
    words = stuff.split(' ')
    print(">>>> val of words->", repr(words)) #debugging
    return words

def sortwords(words):
    sortd = sorted(words)
    return sortd

def print_first_word_pop(words):
    print(words.pop(0))

def print_last_word_pop(words):
    print(words.pop(-1))

stuff = input("Please type your sentence>> ")
words = breakup(stuff)
sorted_words = sortwords(words)

print("Your sentence words are:\n", words)

print("Your sentence words sorted are: \n", sorted_words)

print("The first word of sorted sentence is:", end=' ')
print_first_word_pop(sorted_words)

print("The last word of sorted sentence is:", end=' ')
print_last_word_pop(sorted_words)

print("The NEW first word of sorted sentence is:", end=' ')
print_first_word_pop(sorted_words)

print("The NEW last word of sorted sentence is:", end=' ')
print_last_word_pop(sorted_words)
