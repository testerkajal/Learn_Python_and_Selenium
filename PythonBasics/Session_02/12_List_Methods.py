"""
There are so many methods use in list e.g
1) list.append(x): Add an item to the end of the list. Equivalent to a[len(a):] = [x].
2) list.extend(iterable):extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
3) list.insert(i, x):
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
4)list.remove(x):
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
5) list.pop([i]):
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)
6) list.clear()
Remove all items from the list. Equivalent to del a[:].
7) list.index(x[, start[, end]]):
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.
The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
8) list.count(x):
Return the number of times x appears in the list.
9) list.sort(*, key=None, reverse=False):
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
10) list.reverse():
Reverse the elements of the list in place.
11) list.copy():
Return a shallow copy of the list. Equivalent to a[:].
"""
# 1) list.append(x):
cities=["Delhi","Mumbai","Kolkata","Meerut"]
cities.append("Lucknow") #['Delhi', 'Mumbai', 'Kolkata', 'Meerut', 'Lucknow']
print(cities)

# 2) list.insert(i, x): To insert item at given position
cities.insert(1,"Gurugram") #insert Gurugram at 1st index i.e ['Delhi', 'Gurugram', 'Mumbai', 'Kolkata', 'Meerut', 'Lucknow']
print(cities)

# 3) list.remove(x): remove specified item from the list
cities.remove("Meerut") #['Delhi', 'Gurugram', 'Mumbai', 'Kolkata', 'Lucknow']
print(cities)

# 4) list.reverse(): It will reverse the list items in place
cities.reverse() #['Lucknow', 'Kolkata', 'Mumbai', 'Gurugram', 'Delhi']
print(cities)

# 5) list.clear(): Remove all items from the list. Equivalent to del a[:].
# cities.clear(); #return empty list
# print((cities))

# 6) list.copy(): Return a shallow copy of the list. Equivalent to a[:].
cities.copy()
print(cities)

# 6) list.pop(x): It will pop the last item from the list
cities.pop()
print(cities) #['Lucknow', 'Kolkata', 'Mumbai', 'Gurugram']
#you can sepcify the index as well. i.e cities.pop([i])

# 7) list.pop(x): It will sort the last item in alphabetical order
cities.sort()
print(cities)

# 8) list.count(x): Return the number of times x appears in the list.
Citycount= cities.count("Lucknow")
print(Citycount)
