# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

"""------len(s):------
 The len() function returns the number of items in an object.
if the object is the string then it return the length of the string """

x= "This is my new mackbook"
print(len(x)) #please note it will count the space as well

"""------str():------
this will convert the specified vaue into the string"""
y= 7895289
print(type(str(y))) # here y value is converted to string while it was a nu. + we have checked its type as well.

"""------upper():------
this will convert the value to upper case """
print(x.upper())

"""----# count()----
Returns the number of times a specified value occurs in a string"""
Address ="Gold coast Rohta road meerut"
Address1 ="Gold coast-Rohta road meerut"
print(Address.count('Gold')) # this will count how many times Gold came in the string value address
#If we want to search it within any sepcified substring then
print(Address.count("coast",1,12)) # coast is the word i am searching + 1 is starting index and 12 is the end index till where it will search fr the word.


"""----split()----
Splits the string at the specified separator, and returns a list"""

print(Address.split()) # This will split the string by space. i.e ['Gold', 'coast', 'Rohta', 'road', 'meerut']
print(Address1.split("-")) # This will split the string by -. i.e ['Gold coast', 'Rohta road meerut']

"""----strip()	
Returns a trimmed version of the string"""
d= "     777 tester kajal 777 "
print(d.strip()) #If we don't specify any char than it will remove all the leading and trailing white spaces
print(d.rstrip()) # this will remove the char yo specify from the right of the string. if no char specidied then remove all spaces from right
print(d.rstrip(';7 \'')) #This will remve all 7 from the right
print(d.lstrip(';7 \''))  #This will remve all 7 from the left
print(d.lstrip()) # this will remove the char yo specify from the left of the string. if no char specidied then remove all spaces from left

"""----replace()	
replace any substring with some other"""
t = "tester Kajal tester kchaudhary tester kSingh"
print(t.replace("tester","QA")) #This will replace tester with QA in the whole string
print(t.replace("tester","QA" , 2 )) #This will replace first 2 tester with QA from the whole string

"""----find() and index()----
This 2 works similary both return the index of any substring we are looking for"""
print(t.find("Kajal")) #note return -1 if not found. it will not count the space.
print(t.index("Kajal")) #note return -1 if not found. it will not count the space.
