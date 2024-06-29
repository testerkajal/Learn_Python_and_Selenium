# A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.
# First-Out property. Each value inside the list is called Item.
# List can store any data type value separated by, and enclosed in [].


states_of_America = ["Florida","California","Texas","Ohio","Alabama","Virginia"]
print(states_of_America[1]) #To print the 2nd element
print(states_of_America[-1])# To print the last element of the list

#setting up the off set helps to Move the specified amount of elements to the end of the list.

states_of_America[0] = "Pencinlavenia"
print(states_of_America)

#to append the element at the end of the list
states_of_America.append("New York")
print(states_of_America)

#to add multiple element once in the existing list
states_of_America.extend(["Utah","New Maxico","Nevada"])


# To pop the element first element
states_of_America.pop() #By default it will pop the last element
print(states_of_America)

#to pop some sepecific element
states_of_America.pop(1) #will give the index no of the element that we want to pop
print(states_of_America)





