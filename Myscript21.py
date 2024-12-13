# Dobbelstenen met functies in ander bestand random

import dice

zijden = int ( input ("How many sides on your dice? Max 120, please! "))
getal = int ( input ("How many rolls? "))
dice.roll_multiple(zijden, getal)

print ("enkele roll: ")
dice.roll_1(zijden)


