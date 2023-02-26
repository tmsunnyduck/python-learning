'''
Topics covered : basic operations on lists
.aapend() .insert(item,index) del pop() .remove() .sort() sorted()
.reverse() len()
lists are indexed, mutable and often contain multiple items
'''
days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
print(days)
# to access elements of a list, use its index in []
print(days[0].upper()) 

# index '-1' is used for last element, -2 for second last and so on
print(days[-2])

# modifying elements : just assign it the required vale
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# appending items to list use .append(item)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('Harley')
print(motorcycles)

#inserting item at a position use .insert(index,item)
linux_distros = ['ubuntu','debian','arch']
linux_distros.insert(1,'fedora')
print(linux_distros)

# removing an item using del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

# pop() removes last item from the list, pop(index) pops that element
# pop() allows us to use the popped element before deletion
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print(motorcycles)

# remove(item) searches for item in the list and deletes it
# remove() only deletes first occurence
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

# We can also pass in variables in the .remove()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

# .sort() permanently sorts a list
# preferably use lower case when sorting alphabetical lists
cars = ['bmw','audi','subaru','toyota']
cars.sort()
print(cars)

# use .sort(reverse=True) for sorting in reverse order
cars = ['bmw','audi','subaru','toyota']
cars.sort(reverse=True)
print(cars)

# use the sorted() function to temporarily sort a list
d_110 = ['tushar','vaibhav','jayprakash']
print("Original list :",d_110)
print("Sorted list : ",sorted(d_110,reverse=True))
print("Original list again : ",d_110)

# if you want to simply reverse a list, use .reverse(), chnage permanent
books = ['HC verma','DC pandey','RD sharma']
books.reverse()
print(books)

# use len() to find lenght of a list
houses = ['Gryffindor','Hufflepuff','Ravenclaw','Slytherin']
print(len(houses))
