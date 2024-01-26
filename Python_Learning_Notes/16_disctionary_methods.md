### clear(): Removes all the elements from the dictionary
###
```py
demo_dict1 = {"name":"kajal","age":26,"JobRole":"QA"}
demo_dict1.clear()
print(demo_dict1)
result: {}
```

### copy(): Returns a copy of the dictionary
```py
demo_dict2 = {"1":"kajal","age":26,"3":"QA"}
demo_dict2.copy()
print(demo_dict2)
result: {'1': 'kajal', 'age': 26, '3': 'QA'}
```

### fromkeys(): Returns a dictionary with the specified keys and value
```py
demo_dict2 = {"1":"kajal","age":26,"3":"QA"}
print(demo_dict2.fromkeys("1","kajal"))
result: {'1': 'kajal'}
```

### get(): Returns the value of the specified key
```py
demo_dict3 = {"1":"kajal",1:2,"3":"4"}
print(demo_dict3.get(1))
result: 2
```
### items(): Returns a list containing a tuple for each key value pair
```py
demo_dict6={'a':'b','b':'c'}
print(demo_dict6.items())
result: dict_items([('a', 'b'), ('b', 'c')])
```
### keys(): Returns a list containing the dictionary's keys
```py
demo_dict3 = {"1":"kajal",1:2,"3":"4"}
print(demo_dict3.keys())
result: dict_keys(['1', 1, '3'])
```
### popitem(): Removes the last inserted key-value pair
```py
demo_dict4= {10:10,11:11,12:12}
demo_dict4.popitem()
print(demo_dict4) 
result: {10: 10, 11: 11}
```
### setdefault(): Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
```py
demo_dict5 = {"city":"delhi","pin":"201009"}
x = demo_dict5.setdefault("city","delhi") #here the key  exist so it will return the value of the key.
print(x)
result: delhi

y = demo_dict5.setdefault("district","meerut") #here the key does not exist so it will return the  value of the new key.
print(y)
result: meerut

```

### update(): Updates the dictionary with the specified key-value pairs
```py
demo_dict5= {13:13,14:11,15:15}
demo_dict5.update({14:14})
print(demo_dict5)
result: {13: 13, 14: 14, 15: 15}
```
## values(): Returns a list of all the values in the dictionary
```py
print(demo_dict5.values())
result: dict_values([13, 14, 15])
```




