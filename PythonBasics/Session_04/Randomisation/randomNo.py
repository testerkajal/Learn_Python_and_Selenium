import random
#To print the random whole no or int
a = random.randint(10,20)
print(a)

#To print the random floting no
b = random.random() # by default, it will print floating point no only between 0 and 1
print(b)

#But if we want to print a floting point no between 0 and 2
c = random.uniform(0,2.0) #we will use uniform for this
print(c)

# Love Calculator
love_cal = random.randint(1,100)
print(f"your love score is: {love_cal}")