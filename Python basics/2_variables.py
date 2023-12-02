# variables - variable data type
# variables can refer to any data type
# simple functions in working with variables

# create a variable 'x' and give it a value of '1'
x = 1
print (x)
# resualt: 1

# change the value of the variable 'x'
x = 5
print (x)
# resualt: 5

# create a new variable 'y' and give it a value of '2'
y = 2
print (y)
# resualt: 2

# add the two variables
print (x+y)
# resualt: 7

# you can summarize the same variable
print (x+x)
# resualt: 10

# changing the value of a variable by adding it to itself
x = x+x
print (x)
# resualt: 10

# displaying information about the type of variable 'x'
print (type(x))
# resualt: class 'int'

# changing the value of a variable and displaying information about the type of variable 'x'
x = 1.2
print (type(x))
# resualt: class 'float'

# also variables can consist not only of numbers
z = 'abc'
print (z)
# resualt: abc

# but we can't add variables with different data types, it causes an error
# print(x+z)
# resualt: TypeError

# using variables, you can solve problems such as calculating the perimeter and area of a triangle with sides 'a' 'b'' 'c'
a = 10
b = 5
c = 7
perimeter = a+b+c
p = (a+b+c)/2
# connect the math module to call the 'sqrt' function
import math
area = math.sqrt(p*(p-a)*(p-b)*(p-c))
print (perimeter)
print (area)




d=input("print x" )