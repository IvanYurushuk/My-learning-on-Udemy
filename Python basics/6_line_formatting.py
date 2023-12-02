# String formating

# string formatting examples
print ("My name is {}".format("Ivan"))
# result: My name is Ivan
my_name = "Ivan"
print ("My name is {}".format(my_name))
# result: My name is Ivan
print ("My name is {} and I'm {}".format(my_name, 30))
# result: My name is Ivan and I'm 30

# variable numbering during formatting
print ("My name is {0} and I'm {1}".format(my_name, 30))
# result: My name is Ivan and I'm 30
print ("My name is {1} and I'm {0}".format(my_name, 30))
# result: My name is 30 and I'm Ivan

# number formatting
pi = 3.1415
print ("pi equals {pi:1.2f}".format(pi=pi))
# result: pi equals 3.14

# a popular and simple formatting method
name = 'Ivan'
age = 30
print (f"My name is {name} and I'm {age}")
# result: My name is Ivan and I'm 30
print (f"pi equals {pi:1.2f}")
# resualt: pi equals 3.14