demo_tuple1 = ("kajal",1,1,2,3,False)
demo_tuple2 = ("kajal",1)
#----Count----
print(demo_tuple1.count(1)) #To check the occurance of 1 in the tuple i.e 2
#----index----
print(demo_tuple1.index(2)) #To check the index of 2 in the tuple i.e
#----contains----
print(demo_tuple1.__contains__(demo_tuple2)) #To check whether demo_tuple1 contains "kajal" i.e true


#To join 2 tuples
joined_tuple = demo_tuple1 + demo_tuple2
print(joined_tuple) # i.e ('kajal', 1, 1, 2, 3, False, 'kajal', 1)

#To reverse the tuple items
x = ('apple', 'banana', 'cherry')
result = reversed(x)
result = tuple(result)
print(result)






