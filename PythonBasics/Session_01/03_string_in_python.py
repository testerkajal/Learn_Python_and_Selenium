x = 'My Name is Kajal'
y = ("My name is Meenakshi")

#In python strings are treated as array.
print(x[1]) # so you can access any of the index value i.e y

#handle single and dowble quotes inside any of the string
a= "I am a 'student'" # for single quotes use double outer quotes
b= 'I am a "doctor"' # for double quotes use single outer quotes.
c= 'I am a \'doctor\'' # but if you want to use single quotes inside single quotes. ca use escape characters i.e /
print(a)
print(b)
print(c)

#Here we can use membership operator to check whether any word exist in the string or not.
print("is" in c) #it will return false asßß is doesn't exist in c'