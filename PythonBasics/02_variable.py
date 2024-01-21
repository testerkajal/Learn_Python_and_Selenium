import keyword

keywordlist = keyword.kwlist
print(keywordlist) #here you can get all the reserved keyword list for python that you can't use as varibale name


#To check whether any particular vahriable is keyword or not
print(keyword.iskeyword("return")) #this will return true.



#In oython we don't need to specify the datatype
userName = "kchaudhary21"
#For print in console we simple use print
print(userName)

#To check the data type of any variable
print(type(userName)) #<class 'str'>
#In Python we can reassign the value to any variable.
x=600
print(x)
x=800
print(x)
y=900
print(id(y)) #4367769328
#toconfirm the address of these 2 variables in the memory
print(id(x)) #4343324400
y=x
print(id(y)) #here both x and y has same address #4343324400

#--------Varibale naming convention--------
#1) Python variables are case sensitive
#Class_Name , CLASS_NAME, class_name all these are different variables.

#2) You can't start a variable name with a no. e.g 6ClassName
#)3) You can use _ in the start mid and end of the variable name all are valid.
# 4) You can use alphanumaeric, numbers and letter in varibale name. e.g
_ClassName="1st"

#5) Youbcan't use reserved keywords as varibales. for reserved keyword name you can find the same in lib folder with file name keyword.py.
#return ="test" here return is reserved keyword in python you can't use this variable name


