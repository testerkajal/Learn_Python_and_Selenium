# clear(): Removes all the elements from the dictionary
demo_dict1 = {"name":"kajal","age":26,"JobRole":"QA"}
demo_dict1.clear()
print(demo_dict1) #return {}

# copy(): Returns a copy of the dictionary
demo_dict2 = {"1":"kajal","age":26,"3":"QA"}
demo_dict1.copy()
print(demo_dict2)

# fromkeys()	Returns a dictionary with the specified keys and value
print(demo_dict2.fromkeys("1","kajal")) #{'1': 'kajal'}

# get()	Returns the value of the specified key
demo_dict3 = {"1":"kajal",1:2,"3":"4"}
demo_dict3.get(1)
print(demo_dict3)


# items()	Returns a list containing a tuple for each key value pair
demo_dict6={'a':'b','b':'c'}
print(demo_dict6.items()) #i.e dict_items([('a', 'b'), ('b', 'c')])

# keys()	Returns a list containing the dictionary's keys
print(demo_dict3.keys()) #dict_keys(['1', 1, '3'])

# popitem()	Removes the last inserted key-value pair
demo_dict4= {10:10,11:11,12:12}
demo_dict4.popitem()
print(demo_dict4) #{10: 10, 11: 11}

# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
demo_dict5 = {"city":"delhi","pin":"201009"}
x = demo_dict5.setdefault("city","delhi") #here the key  exist so it will return the value of the key.
print(x)
y = demo_dict5.setdefault("district","meerut") #here the key does not exist so it will return the  value of the new key.
print(y)

# update()	Updates the dictionary with the specified key-value pairs
demo_dict5= {13:13,14:11,15:15}
demo_dict5.update({14:14})
print(demo_dict5)

# values()	Returns a list of all the values in the dictionary
print(demo_dict5.values())




