x = "Python Class"
y = "tester kajal"
z= "learn"
#Now i want to print "Start Python Class with tester kajal

# with traditional method
print("Start "+x+" with "+y)

#With string literals
print("Start %s with %s" %(x,y)) #here first %s will replaced with x and 2nd %s will replaced with y
print("Start %s with %s" %("java class",y)) #here we can give the cudtomised value as well.

#----We can do the same thing with string format methods in string.
print("Welcome to {} and {} with {}".format(x,z,y))

#If there are too many variable to be relace than the below syntax is recommended
print("Welcome to {0} and {2} with {1}".format(x,y,z)) # here 0,1,2 tell the index of the variable defined to be passed.

#To amke the above syntax readable use the below syntax
print("Welcome to {className} and {job} with {teacher}".format(className=x,teacher=y,job=z))