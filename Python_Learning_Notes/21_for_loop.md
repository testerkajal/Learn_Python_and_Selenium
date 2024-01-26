### Used to iterate over the sequence like list, string, dictionary set tuples etc.

### String
```py
city1 = "delhi" #for string
```
### list
```py
city_2 = ["delhi","kolkata","mumbai"] 
```
### tuples
```py
city_3 = [["dehi","delhi"],["up","ghaziabad"]] 
```
### dictionary
```py
demo_dict1 = {"name":"kajal","age":26,"JobRole":"QA"} 
```

## Example1
```py
city1 = "delhi" 
for c in city1: 
    print(c)
result: 
d
e
l
h
i
```
## Example2
```py
city_2 = ["delhi","kolkata","mumbai"] 
for c in city_2: 
    print(c)
result:
delhi
kolkata
mumbai
```
## Example3
```py
city_3 = [["dehi","delhi"],["up","ghaziabad"]] 
for district, city in city_3: 
   print(f"{district},{city}")
result:
dehi,delhi
up,ghaziabad
```
## Example4
```py
# we used items to un packed the data for more than 2 items.
demo_dict1 = {"name":"kajal","age":26,"JobRole":"QA"} 
for key, value in demo_dict1.items():  
         print(f"{key}:{value}")
result:
name:kajal
age:26
JobRole:QA

```