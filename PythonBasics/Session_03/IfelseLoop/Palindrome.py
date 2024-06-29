#Write a program to check if the given number is palindrome or not.

input_string = input("Enter a string: ")

def is_palindrome(s):
    return s == s[::-1]

if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")