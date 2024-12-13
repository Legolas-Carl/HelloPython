#Dictionary oefening

planet = {
    'Mercury': 0.39,
    'Venus': 0.72,
    'Earth': 1.00,
    'Mars': 1.52,
    'Jupiter': 5.2,
    'Saturn': 9.58,
    'Uranus': 19.20,
    'Neptune': 30.05
}

q1 = input("Enter a Planet: ")
print (q1 + " is " + str(planet[q1]) + " au (or " + str(149597871*planet[q1])  + " km) from the sun")

#Oplossing Siebe

planet_distances={
    'mercury': 0.39,
    'venus': 0.72,
    'earth': 1.00,
    'mars': 1.52,
    'jupiter': 5.2,
    'saturn': 9.58,
    'uranus': 19.20,
    'neptune': 30.05
}

q1 = input("Choose a planet: ")
planet_distance = planet_distances[q1]
print(f"{q1} is {planet_distance} au (or {planet_distance * 149597870.7}km) from the sun")