def die(sides):

    import random

    print(f"Rolling {sides}-sided die: {random.randint(1,sides)}")

    answer = input("Roll again?(y/n): ")

    while answer != 'n':
        if answer == 'y':
            print(f"Rolling {sides}-sided die: {random.randint(1, sides)}")
        answer = input("Roll again?(y/n): ")

def roll_1(sides):
    import random
    print(f"Rolling {sides}-sided die: {random.randint(1,sides)}")

def roll_multiple(sides, rolls):
    i=1
    import random
    while i <= rolls:
        print(f"Rolling {sides}-sided die, roll {i} : {random.randint(1,sides)}")
        i += 1
