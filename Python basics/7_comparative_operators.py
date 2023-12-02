# Comparative operators

# comparison marks
# > greater
# < less
# >= greater or equal
# <= less or equal
# == equal
# != not equal
print (2>1)
# resualt: True
resualt = 2>1 
print (type (resualt))
# resualt: <class: 'bool'>
print (2>2)
# resualt: False
print (2>=2)
# resualt: True
print (3>=2)
# resualt: True
print (3 >= 4)
# resualt: False
print (1 != 1)
# resualt: False
print (2 != 1)
# resualt: True

# you can compare strings
print ("name"=="name")
# resualt: True
print ("name"=="another name")
# resualt: False
print ("name" == "Name")
# resualt: False
x = 'Name'
y = 'name'
print (x.lower() == y.lower())
# resualt: True

# multivariate comparison
print (1<2<3)
# resualt: True
print (1<2>3)
# resualt: False
# a more readable way to compare multiple variables
print (1<2 and 2<3)
# resualt: True
print (1>2 and 2<3)
# resualt: False

# Comparison method, where one of the comparison results is taken into account
# If at least one comparison is correct, the full comparison is considered correct
print (1>2 or 2<3)
# resualt: True
print (1>2 or 2>3)
# resualt: False