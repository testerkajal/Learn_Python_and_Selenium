#-----syntax----
"""while expression:
      body statement to be executed"""

#-------Example1------
x = 0
while x<=10:
    print(x)
    x+=1
print("x is > 10, so we are out of the loop")

#-------Example2------

city = "Delhi"
x = 0
while x < len(city):
    print(city[x])
    x = x + 1

#-------Example3 with list------

city = ["Delhi","mumbai","kolkata"]
x = 0
while x < len(city)-1:
    print(city[x]) #Delhi mumbai
    x = x + 1

