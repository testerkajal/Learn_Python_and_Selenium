# Arithmatic Operator
# Assignment Operator
# Comparison operator
# Logical Operator
# Bitwise Operator
# Membership Operator
# Identity Operator

# Arithmatic Operator
x = 15
y = 6
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y) #retrun mod
print(x ** y) # exponent
print(x // y) #floor division it will round off and give result as a whole no.

# Assignment Operator
x=2
x+=2
print (x)
x-=2
print (x)
x*=2
print (x)
x/=2
print (x)

# Comparison operator
a=5
b=6
print(a==b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a!=b)

#Logical operator (And/ or)
print(a == b and a>b)
print(a == b or a<b)

# Identity Operator(is / ==)
u=["kajal","Meenu"]
v =["kajal","Meenu"]
c=["kajal","sumit"]
print(u == v) # this compares the data
print(v is c) # this compares the objects as both are seperate obj so return false
print(v is not c) # this compares the objects

# Bitwise Operator (This works basically on binary nos.)
# & as and
# | as OR
t=0
w=1
print(t & w) #0*1
print(t | w) #0+1



# Membership Operator
#To check wheteher any value is the member of  any list
print("Meenu" in u) # return true as u contains meenu
print("Meenu" not in u) # return false as u contains meenu


