import random

number = random.randint (1, 20)

guess = 0

while guess != number:
    guess = int(input("geef een nummer tussen 1 en 20 in: "))
    if guess > number:
        print ("Lower")
    elif guess < number:
        print ("Higher")

print ("Geraden")