#Write a program to find the given number is positive or negative.

num = float(input("Enter a num: "))
if(num>0):
    print(f"{num}: is positive")
elif num==0:
    print(f"{num}: is zero")
else:
    print(f"{num}: is negative")

'''
In the given code, the use of float for input is a design choice that allows the program to handle both integers and floating-point numbers. 
When you use float(input("Enter a num: ")), the user can input either an integer or a floating-point number.'''