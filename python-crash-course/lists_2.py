'''
Topic covered : working with lists
see lists.py for list basics
'''

# looping through entire list use for loop
magicians = ['alice', 'david', 'carolina']

# here magician is a temporary variable (like int i used in C)
for magician in magicians :
    print(magician) # prints each item in the list

for magician in magicians :
    print(f"{magician.title()}, that was a great trick!")
