# set.add(): To add any item in the set
set1 ={"kajal",20,"meenu","sristi"}
set1.add("kajal") # this will not work as kajal already exist in the set
set1.add("Neha")
print(set1)

# set.pop(): To remove first element from the left in the set
set2={1,2,3,4,5}
set2.pop()
print(set2)

#set.remove(4): to remove any articular value from the set
set3={2,4,5,7}
set2.remove(4)
print(set2)

#set.clear(): To empty the set
set4 ={1,2,3}
set4.clear()
print(set4)

#set.update(): To empty the set
set5 = {"kajal","test",1,2}
set5.update(set5)
print(set5)

#set.union(): To join 2 sets
demo_set1 = {1,2,3}
demo_set2 ={1,7,6}
new_set = demo_set1.union(demo_set2) #While joining 2 sets it will take the duplicate data only once.
print(new_set) #i.e {1, 2, 3, 5, 6}

#set.Intersection(): To take common value from 2 sets
new_set1 = demo_set1.intersection(demo_set2)
print(new_set1) #i.e {1}

#set.difference(): It will check what value doesn't exist in another set
new_set2 = demo_set1.difference(demo_set2) #{2, 3} as 2,3 not exist in set2
new_set3 = demo_set2.difference(demo_set1) # {7,6} as 7,6 not exist in set1
print(new_set2)
print(new_set3)

#set.issuperset(): It will check whether any set is superset of another set
test_set1 = {1,2,3,4,5}
test_set2 ={1,2}
print(test_set1.issuperset(test_set2)) # it will return true as all values set 2 exist in set 1
print(test_set2.issuperset(test_set1)) # it will return false as all values of set 2 doesn't exist in set 1

#set.issubset(): It will check whether any set is superset of another set
print(test_set1.issubset(test_set2)) # it will return false as all values set 1 exist in set 2
print(test_set2.issubset(test_set1))  # it will return false as all values set 2 exist in set 1


