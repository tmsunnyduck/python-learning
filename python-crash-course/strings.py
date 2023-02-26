'''
Topics covered : basic operation on string
.title() .upper() .lower() .rstrip() .lstrip() .strip()
.removesuffix(), .removeprefix()
'''

name = "ada Lovelace"

print(name.title()) # converts to title case
print(name.upper()) # converts to upper case
print(name.lower()) # converts to lower case

# f-strings are used to insert a variable's value as a string

first_name = "charles"
last_name = "babbage"

# a 'f' is placed in front of the string to format it,
# variables are written inside a '{}'
full_name = f"{first_name} {last_name}" # behaves as a normal string
print(full_name.title())

message = f"{full_name.title()} is known as the father of computer"
print(message)

# escape sequences :
# \n for newline, \t for a tab
print("Languages: \n\tPython\n\tC\n\tJabascript")

# strip whitespace from the right with .rstrip() and left with .lstrip()
language_right_whitespace = "python "
language_left_whitespace = " python"

print(language_right_whitespace.rstrip())
print(language_left_whitespace.lstrip())

# strip from both left and right with .strip()
language_strip = " python "
print(language_strip.strip())

# remove prefixes with .removeprefix('the prefix to remove')
# remove suffix with .removesuffix('the suffix to remove')
website_url = "https://python.org"
print(website_url.removeprefix('https://'))
print(website_url.removesuffix('.org'))



