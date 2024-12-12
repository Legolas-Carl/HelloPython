fruit = "tekst"
fruits = ["Apple", "Pear","Pineapple", "Raspberry", "Strawberry"]

print("My favourite fruit is " + fruits[3])

fruits.append ("Kersen")
fruits.append ("Appelsienen")
fruits.append ("Mandarijnen")

print(fruits)

fruits[5] = "Cherry"
fruits[6] = "Orange"
fruits[7] = "Mandarin"

print(fruits)

del fruits[7]

print(fruits)

print(len(fruits))

for fruit in fruits:
    print(fruit)

