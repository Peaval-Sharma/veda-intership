a=input("Enter a user name:-")
n=int(input("Enter a number which you want to check: "))
if n<0:
    print("Negative numbers cannot be prime number.")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            break
    else:
        print(f"{n} is a prime number.")
print("your numbeer is successfully checked.")
