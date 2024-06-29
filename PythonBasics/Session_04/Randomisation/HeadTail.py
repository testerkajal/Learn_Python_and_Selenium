# Here we will do interactive coding exercise: Head and Tail.
# here our program will tell us head or tail randomly
# Hint: Remember to import random no first.

import random
num = random.randint(0,1) # here we are tail a random no and then based on that no using conditional stmt
if num ==1:
    print("Head")
else:
    print("Tail")