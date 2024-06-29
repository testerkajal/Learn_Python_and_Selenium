size = (input("Enter the size of pizza\n"))
add_peperoni = input()
extra_cheese = input()

# for small = 180rs, M = 280, L = 420
# for peperoni = 20 FOR M and Large =  30  , for cheese = 50 and for M and L =  "80"
bill = 0
if size == "S":
    bill += 180
elif size == "M":
    bill += 280
else:
    bill += 420

if add_peperoni == "Y":
    if size == "S":
        bill += 20
    else:
        bill += 30

if extra_cheese == "Y":
    if size == "S":
        bill += 50
    else:
        bill += 80

print(f"final bill: ${bill}")
