"""
# Set is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
* Note: Set items are unchangeable, but you can remove items and add new items.
Note: Sets are unordered, so you cannot be sure in which order the items will appear.
Notes: Duplicates Not Allowed
Note: Sets are declared with {}
Note: set can hold data with different data type

"""
set1 = {"kajal",20,20,10.1,"Kajal"}
print(set1) # It will print only the unique items.
# Please note sets are case sensitive. i.e kajal and Kajal both are considered as 2 diff values
#Items can be printed in any order as sets are unordered.


#To create an empty set you can use.
set2 = set(("kajal","Meenu")) #result can be {'kajal', 'Meenu'} or {'Meenu', 'kajal'} as set is unordered
set3 = set(("kajal")) #{'l', 'j', 'a', 'k'} or {'l', 'k', 'a', 'j'} as set is unordered
set4 = set(("")) #Empty set
print(set2)
print(set3) #This will print result like
print(set4)

#To check the length of the set
print(len(set1)) #Note: It will not count the duplicate items

#To use the membership operator
print("kajal" in set1) #True as kajal exist in set 1
