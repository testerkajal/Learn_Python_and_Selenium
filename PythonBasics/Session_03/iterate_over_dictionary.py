obj = [
    {1: "test", 2: "test2", 3: "test2"},
    {'a': "A", 'b': "B", 'c': "C"}
]
# to print the key value pair of item 1
for item in obj:
 print(item)

 #to print the key, value pair of each item inside each obj
 for key, value in item.items():
     print(f"{key}:{value}")



