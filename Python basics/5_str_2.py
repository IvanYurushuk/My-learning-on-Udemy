# Functions for working with strings


# create a string
x = 'Hello, my name is Ivan'

# function to calculate string length
print (len(x))
# resualt: 22

# function for finding a specific index
print (x.count('l'))
# resualt: 2 

# function that makes the first letter of a string uppercase, the rest lowercase
a = x.capitalize()
print (a)
# resualt: Hello, my name is ivan

# function that makes all letters uppercase
a = x.upper()
print (a)
# resualt: HELLO, MY NAME IS IVAN

#function that makes all letters lowercase
a = x.lower()
print (a)
# resualt: hello, my name is ivan

# Checking strings for upper or lower case
upper = x.upper()
lower = x.lower()
print (x.isupper())
# resualt: False
print (x.islower())
# resualt: False
print (upper.isupper())
# resualt: True
print (lower.islower())
# resualt: True

# index search functions
print (x.find('l'))
# resualt: 2 
print (x.find('l', 1))
# resualt: 2
print (x.find('l', 1, 5))
# resualt: 2
print (x.find('l', 5, 10))
# resualt: -1
print (x.find('m', 7, 15))
# resualt: 7
print (x.find('m', 8, 15))
# resualt: 12
print (x.find('my'))
# resualt: 7

# checking the function for the presence or absence of letters and numbers
# .isalnum determines whether the function consists of only letters and numbers
# .isalpha determines whether the function consists only of letters
print ('123abc'.isalnum())
# resualt: True
print ('123abc!'.isalnum())
# resualt: False
print ('123abc'.isalpha())
# resualt: False
print ('abc'.isalpha())
# resualt: True

# string empty check
print ('   '.isspace())
# resualt: True
print (''.isspace())
# resualt: False

# string empty check
empty_string = ''
print (empty_string == '')
# resualt: True

# more accurate string empty check
# .strip removes indices from the string specified in brackets
empty_string2 = '   '
print (empty_string.strip(' ') == '')
# resualt: True

# check strings for start and end indices
h = 'hello'
print (h.startswith('he'))
# resualt: True
print (h.endswith('lo'))
# resualt: True

# .split function splits a string by a specified index
split = h.split('l')
print (split)
# resualt: ['he', '', 'o']
split = h.split('e')
print (split)
# resualt: ['h', 'llo']
# .split function makes a variable of data type list from a string
print (type(split))
# resualt: <class 'list'>
# example of using the .split function
data = '12.10.58.156'
separated_data = data.split('.')
print (separated_data)
# resualt: ['12', '10', '58', '156']

# .partition function divides the string by index, preserving the index
python = 'Python is fan'
print (python.partition('is '))
# resualt: ('Python', 'is', 'fun')
print (python.partition('not '))
# resualt: ('Python is fan')
python = "Python is fun, isn't it"
print (python.partition('is'))
# resualt:('Python', 'is', "fun, isn't it")