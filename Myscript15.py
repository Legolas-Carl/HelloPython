cities = ["Austin", "Busan", "Casablanca", "Damascus", "Izmir", "Madrid", "Palermo"]
city = "Amsterdam"

print ("i.   " + str(cities[:2]))
print ("ii.  " + str(cities[1:3]))
print ("iii. " + str(cities[:-2]))
print ("iv.  " + str(cities[-4]))
print ("v.   " + str(cities[-3:-1]))
print ("vi.  " + str(cities[2:0]))

# Mijn Oplossing

sentence = "Ik heb de volgende steden al bezocht: "
for city in cities[:-1]:
    sentence = sentence + city + ", "

sentence = sentence + "and " + cities [-1] + "."
print (sentence)

#oplossing van Siebe

print("On my world tour I visited ",end="")

for stad in cities[:-2]:
    print(stad, end=', ')
print(cities[-2], end=' ')
print('and ' + cities[-1] + '.')

#die end=" " spatie toevoegen zonder newline
