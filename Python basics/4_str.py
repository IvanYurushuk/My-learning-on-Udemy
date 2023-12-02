# The most popular data type is strings
# Strings take up more memory
# Strings immutable data type

# strings can be written in single and double quotation marks
a = 'Ivan'
b = "Ivan"
print (a)
# resualt: Ivan
print (b)
# resualt: Ivan

# if single or double quotation marks are used in the string itself, the outer quotation marks must be reversed
c = "I'm Ivan"
print (c)
# resualt: I'm Ivan
d = 'Ivan is "strong" programmer'
print (d)
# resualt: Ivan is "strong" programmer

# If both types of quotation marks are used in a string, a backslash must be used
d = "I'm a \"strong\" programmer"
print (d)
# resualt: I'm a "strong" programmer

# If a backslash already exists, add another backslash next to it
e = 'C:\\Users\\Programm'
print (e)
# resualt: C:\Users\Programm

# simple solution to an old problem
f = r'C:\Users\Programm'
print (f)
# resualt: C:\Users\Programm

# string literal usage
g = "I'm Ivan and \nI'm a programmer"
print (g)
# resualt: I'm Ivan and
#I'm a programmer

# working with row indices
hello = str("Hello. I'm Ivan")
# first index reference
print (hello[0])
# resualt: H
# fourth index reference
print (hello[3])
# resualt: l
# thirteenth index reference
print (hello[12])
# resualt: v
# accessing the thirteenth index in a simple way, using "-"
print (hello[-3])
# resualt: v
# string output from the third index
print (hello[2:])
# resualt:llo. I'm Ivan
# output of the string from the first to the fourth index
print (hello[0:3])
# resualt: Hel
# output a string from the first to the sixteenth index, using every second index
print (hello[0:15:2])
# resualt: Hlo ' vn

# stringing
print ('My name is' + ' ' + 'Ivan')
# resualt: My name is Ivan
# ways to glue together large numbers of strings
h = 'hello'
w = 'world'
print (h + ' ' + w)
# resualt: hello world
print ("%s %s" % (h, w))
# resualt: hello world

# using different types of data you can't get the answer you want
print ('2'*7)
# resualt: 2222222


#
x=input("print x")