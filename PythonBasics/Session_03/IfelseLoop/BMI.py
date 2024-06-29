height = float(input("Enter the height\n")) #in meteres
weight = float (input("Enter the weight\n")) #in kg
BMI = weight/(height*height)
print(BMI)

if BMI <18.28:
    print("Person is slightly underweight")
elif BMI > 18.28 and BMI <22.5:
    print("Person is normal weight")
else:
    print("Person is over weight")
