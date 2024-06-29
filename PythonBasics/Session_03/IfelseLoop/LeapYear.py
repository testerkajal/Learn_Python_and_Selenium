# To check whether a given year is a leap year or not
# A normal year has 365 no of days
# while leap year has 366 no of days

# -----Condition-----
# year divisible by 4 with no reminder +


year = int(input("Enter the year\n"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("year is leap year")
else:
    print("Not a leap year")
