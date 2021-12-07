import random
number = random.randrange(1, 20)
guess = int(input("Enter A Number Between 1 And 20: "))
while guess != number:
    if guess < number:
        print("You Need To Guess Higher")
        guess = int(input("Enter A Number Between 1 And 20: "))
    elif guess > number:
        print("You Need To Guess Lower")
        guess = int(input("Enter A Number Between 1 And 20: "))
else:
        print(f'{number} is The Lucky Number!')



