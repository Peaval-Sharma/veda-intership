a = input("Enter user name:-!")
n = int(input("Enter a number which you want to check: "))

x = n
retult = 0

# Reverse the number
while n > 0:
    remainder = n % 10
    retult = retult * 10 + remainder
    n //= 10

# Palindrome check
if x == retult:
    print(f"{x} is a palindrome number.")
else:
    print(f"{x} is not a palindrome number.")

print("Thank you for using the palindrome number checking system.")
print("Your number is successfully checked.")