'''
4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing CTRL-C or by closing the output window.)
'''
# takes a lot of time to run
list_till_million = [x for x in range(1,1000001)]

for number in list_till_million :
    print(number)
