import random
 
number = random.randint(1, 100)
attempts = 0

print("🎯 Number Guessing Game")
print("Maine 1 se 100 ke beech ek number socha hai.")

while True:
    guess = int(input("Apna guess enter karo: "))
    attempts += 1

    if guess < number:
        print("Bahut chhota number hai! Try again.")
    elif guess > number: 
        print("Bahut bada number hai! Try again.")
    else:
        print("🎉 Congratulations!")
        print("Aapne number guess kar liya:", number)
        print("Total attempts:", attempts)
        break