import calc


bew = input("welke bewerking: +-*/2 ? ")
getal1 = int(input ("Geef getal 1: "))
getal2 = int(input ("Geef getal 2: "))

if bew == "+":
    print (str(calc.add(getal1,getal2)))
elif bew == "-":
    print (str(calc.subtract(getal1,getal2)))
elif bew == "*":
    print (str(calc.multiply(getal1,getal2)))
elif bew == "/":
    print (str(calc.divide(getal1,getal2)))
elif bew == "2":
    print (str(calc.power(getal1,getal2)))
else:
    print ("foute in uw invoer")
