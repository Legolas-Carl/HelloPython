# Dobbelstenen met functie random

import dice

getal = 0
zijden = 5
q1 = "y"

zijden = int ( input ("How many sides on your dice? Max 120, please! "))
# while zijden < 3 or zijden > 120:
dice.roll_1(zijden)



# oplossing Siebe

#import random

#sides = int(input("How many sides?"))
#while sides < 3 or sides > 120:
#    print("Invalid amount of sides!")
#    sides = int(input("How many sides?"))


#print(f"Rolling {sides}-sided die: {random.randint(1,sides)}")

#answer = input("Roll again?(y/n): ")

#while answer != 'n':
#    if answer == 'y':
#        print(f"Rolling {sides}-sided die: {random.randint(1, sides)}")
#    answer = input("Roll again?(y/n): ")

