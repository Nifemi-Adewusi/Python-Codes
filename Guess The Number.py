import random
number = random.randrange(1, 30)
guess = int(input("Enter A Number Between 1 And 30: "))
while guess != number:
    if guess < number:
        print("You Need To Guess Higher")
        guess = int(input("Enter A Number Between 1 And 30: "))
    elif guess > number:
        print("You Need To Guess Lower")
        guess = int(input("Enter A Number Between 1 And 30: "))
else:
        print(f'{number} is The Lucky Number!')



