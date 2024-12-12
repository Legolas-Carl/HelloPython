
european = False
unladen = False

q1 = input("Is the swallow European? Y/N ")
q2 = input("Is the swallow unladen? Y/N ")

if q1 == "y" or q1 == "Y":
    european = True
if q2 == "n" or q2 == "N":
    unladen = True

if european and unladen:
    print("24 miles per hour")
