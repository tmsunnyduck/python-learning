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
    print(f"Thanks for performing {magician.title()}!")

print("loop end")

# Numerical lists

# range(start,end,step) fucntion generates a series of
# integers from start to (end - 1) adding the step value
for value in range(1,5) : 
    print(value)

for even in range(2,11,2) : #adds 2 each iteration
    print(even)
# range() to make a list of numbers
# use the list() to convert the result of range()
# to a list

numbers = list(range(1,6))
print(numbers)

cubes = []
for number in range(1,11) :
    cube = number ** 3
    cubes.append(cube)

print(cubes)

# min() max() and sum() can be performed on a list of numbers
digits = [1,2,3,4,5,6,7,8,9]

print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehension

squares = [value**2 for value in range(1,11)]
print(squares)

# another example
digits = [1,2,3,4,5,6,7,8,9]
arithmetic_progression = [(3*digit + 2) for digit in digits ]
print(arithmetic_progression)

# slicing a list
players= ['Sachin','Virat','Rahul','Rohit']

print(players[1:4]) # Works just like range, starts at index 1 till 3
print(players[:4])
print(players[3:])

