"""used to iterate over the sequence like list, string, dictonary set tuples etc."""

city1 = "delhi" #for string
city_2 = ["delhi","kolkata","mumbai"] #for list
city_3 = [["dehi","delhi"],["up","ghaziabad"]] #for tuples
demo_dict1 = {"name":"kajal","age":26,"JobRole":"QA"} #for disctionry

for c in city1: # here c means character
    print(c)

for c in city_2: # here c means value
    print(c)

for district, city in city_3: # here c means value
    print(district, city)

for key, value in demo_dict1.items():  # we used items to unpacked the data for more than 2 items.
        print(key, value)