
age = int(input("Leeftijd? "))

if age >= 18:
    print ("Volwassen")
elif age >= 10:
    print ("Tiener")
elif age >= 3:
    print ("Kind")
elif age >= 0:
    print ("Baby")
else:
    print ("Verkeerd ;-) ")


gewicht = float(input("Hoeveel kg weeg je?"))
lengte = float(input("Hoe groot ben je in cm"))

lengte /= 100

bmi = round(gewicht/(lengte**2),2)

print("Je BMI is: " + str(bmi))

if bmi < 20:
    print("Je hebnt ondergewicht")
elif bmi < 30:
    print("Je bent ok")
elif bmi < 40:
    print("Je hebt obesitas")
else:
    print("Je hebt ziekelijk overgewicht")
