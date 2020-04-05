# sets var tabby_cat = escape(tab) string
tabby_cat = "\tI'm tabbed in."
# sets var persian_cat = string with escape(new line)
persian_cat = "I'm split\non a line."
# sets var backslash_cat = string with escape(backslashes)
backslash_cat = "I'm \\ a \\ cat."

cats_at_home = "\n {} \n{} \n\n\n\n\n \t\t\t\t\t\t\t\t {}"
# sets var fat_cat = block (""") string with individual rows & bullets
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
# outputs tabby_cat with escape formatting
print(tabby_cat)
# outputs persian_cat with escape formatting
print(persian_cat)
# outputs backslash_cat with escape formatting
print(backslash_cat)
# outputs fat_cat with """ and escape formatting
print(fat_cat)

print(cats_at_home.format(tabby_cat, persian_cat, backslash_cat))
