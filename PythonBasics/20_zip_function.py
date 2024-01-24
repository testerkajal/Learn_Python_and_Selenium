"""The zip() function in Python is used to combine two or more iterable dictionaries into a single iterable,
where corresponding elements from the input iterable are paired together as tuples.
 When using zip() with dictionaries, it pairs the keys and values of the dictionaries based on their position in the dictionary."""

a = [1, 2, ]
b = ["meenu", "kajal", "sumit"]

c = zip(a, b)  # list with lowest no of item decide the new list length
# print(tuple(c)) #to view as tuple i.e ((1, 'meenu'), (2, 'kajal'))
# print(list(c)) #to view as list i.e [(1, 'meenu'), (2, 'kajal')]
print(dict(c))  # to view as dictionary i.e {1: 'meenu', 2: 'kajal'}

# ------Real example------
buying_cost = [45, 50]
selling_cost = [55, 60]

for x, y in (buying_cost, selling_cost):
    print(y - x)  # return 5 5



