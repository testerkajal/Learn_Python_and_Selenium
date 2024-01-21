
"""--------Here are formula of slicing
1) s[startIndex:endIndex] //please note that endindex item will be exclusive.
2) s[startIndex:endIndex:steps] // here steps means how many steps i want to skip 
"""

w = "Here I am learning Python"
print(w[0:-1]) #Here I am learning Pytho.... note excluded lastchar
print(w[0:6]) # Here I
print(w[0:-1:4]) #it will remove every char till next 4th char found butinclude 1st char.

#reversing string in python
print(w[::-1]) #just mention the step as -1 as leave start and endindex as blank.
