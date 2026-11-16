n=input("Enter a user name : ")
temp=int(input("Enter a tempreture : "))
x=input("Enter c for celsius and f for fahrenheit : ")
if x=="c":
    result=(temp*9//5)+32
    print(f"{result} This is your tempreture in celsius.")
elif x=="f":
    result=(temp-32)*5//9
    print(f"{result} This is your tempreture in fahrenheit.")
else:
    print("Invalid input. Please enter 'c' for celsius or 'f' for fahrenheit.")
print("Your temperature is successfully converted.")