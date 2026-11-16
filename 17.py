try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    c = a / b

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result =", c)

finally:
    print("Program execution completed.")