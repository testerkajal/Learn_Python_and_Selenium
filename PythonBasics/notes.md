### How Import libraries works.
1) Import Libraries are just a python file that has it's related functionality code
2) We use that python file in our different python code to call its method variable.

## Example
### we have a random.py file that has below code:
```py 
pi = 3.14
```
###  Now we can use that file in test.py file like below
```py
import random
print(random.pi) // this will take the pi variable value from random.py file and print the result
```