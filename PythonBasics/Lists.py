"""A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.
Each element or value that is inside of a list is called an item.
Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ]
list can store values of different data types"""

z= ["My Name","is","Kajal","and","age",26]
print(z)
print(type(z)) #to check the data type of z i.e <class 'list'>

#We can access the list items with index.
print(z[3]) #and

#Similarly as in string we can use slicing for list as well
print(z[::2]) #It will do the step action from the 0 to end index of the list items and skip printing every secon item of the list.i.e ['My Name', 'Kajal', 'age']

#To reverse the list items just use below syntax as we used for string
print(z[::-1])


