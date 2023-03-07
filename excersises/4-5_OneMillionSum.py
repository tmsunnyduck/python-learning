'''
4-5. Summing a Million: Make a list of the numbers from one to one million, and
then use min() and max() to make sure your list actually starts at one and ends
at one million. Also, use the sum() function to see how quickly Python can add
a million numbers.
'''
list_of_million = [x for x in range(1,1000001)]

print(min(list_of_million))
print(max(list_of_million))
print(sum(list_of_million))
