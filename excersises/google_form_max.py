# takes input and converts to integer using list comprehension
a = [int(x) for x in input().split()] 

print(max(a))

txt = input()

rev_string = txt[::-1]

if txt == rev_string :
    print("Palindrome")
else :
    print("Not a Palindrome")

text = input()

vowels = ['a','e','i','o','u','A','E','I','O','U']

text_no_vowels = ""

for character in text :
    if character not in vowels :
        text_no_vowels = text_no_vowels + character

print(text_no_vowels)

import csv

with open("csv_files.txt", mode='r') as file :

    csv_file = csv.reader(file)

    for line in csv_file :
        print(line)

cp_subjects = {"painting":124, "advertisement":123, "dance":126, "music":125}
print(cp_subjects['advertisement'])

sorted_dict = dict(sorted(cp_subjects.items(), key=lambda x:x[1]))
print(sorted_dict)