num = int(input("Enter a num"))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("Number is not a prime: ", + num)
            break
        else:
            print("Number is prime: ", + num)
            break
