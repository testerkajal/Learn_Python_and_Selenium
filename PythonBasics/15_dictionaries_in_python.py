"""A Python dictionary is a collection of key:value pairs.
They are changeble and don't allow duplicate values
In many other languages, this data structure is called a hash table because its keys are hashable.
"""
"""------What we will cover-----"""
#Defining dictionaries
#Accessing items from the dictionary
#Adding item into the dictionary
#Removing item from the dictionary

#Defining dictionaries It is similar as we do sets. ie {}
demo_dict = {} #Empty dictionary
print(type(demo_dict)) #<class 'dict'>
demo_dict1 = {"name":"kajal","age":26,"JobRole":"QA"} #Empty dictionary

#Accessing items from the dictionary
print(demo_dict1) #to access the whole dictionary
print(demo_dict1["name"]) #To access the item with key. i.e kajal
print(demo_dict1["age"]) #i.e 26


#Adding item into the dictionary
print(demo_dict) #before adding the new key value pair
demo_dict["prod"] = "server71"
demo_dict["test"] = "server147"
print(demo_dict) #after adding the new key value pair


#Removing item into the dictionary
print(demo_dict) #{'prod': 'server71', 'test': 'server147'}
demo_dict.pop("test") #need to mention the key that needs to be removed
print(demo_dict) #{'prod': 'server71'}