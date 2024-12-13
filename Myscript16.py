#Opdracht: verschil tussen een List en een Tuple
#Tuple kan je niet aanpassen, niet append, niet delete, etc.


cities = ("Austin", "Busan", "Casablanca", "Damascus", "Izmir", "Madrid", "Palermo")
steden = []

print (cities[:3])
print (cities[-1])

print ("Bezocht")
for city in cities:
    print (f"\t{city} ")
#\t is een tab


for city in cities:
    steden.append(city)

steden[0] = "Boston"
steden.append("Hellhole")
steden.remove("Casablanca")

print (steden)

#cities = ()
#for city in steden:
#    cities.append