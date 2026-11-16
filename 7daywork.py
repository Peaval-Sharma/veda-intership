password = input("Enter your password: ")

has_number = False
has_alphabet = False
has_special = False
#possible logic to check the password
for ch in password:

    if ch.isdigit():
        has_number = True

    elif ch.isalpha():
        has_alphabet = True

    else:
        has_special = True

if has_number and has_alphabet and has_special:
    print("Valid Password")
else:
    print("Invalid Password")