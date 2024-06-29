#Nested List is basically a list that contains another List inside it.
Fruits = ["Mango","Banana","Papaya","Grapes"]
Vegies = ["Peas", "Tomato","Potato","Carrot","Brinjal"]

Final_List = [Fruits,Vegies]
print(Final_List)

#Access elements from nested list
print(Final_List[0][0]) #It will return 1st elemnt of Fruits list, remember indexing start from 0

print(Final_List[1][1]) #It will return 1st elemnt of vegies list, remember indexing start from 0
