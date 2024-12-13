shopping_list = []
total_cost = 0.0

while True:
    product = input("Welk product wil je toevoegen? ")
    quantity = int(input("Hoeveel wil je hiervan? "))
    price = float(input(f"Hoeveel kost dit {product} ({quantity})? "))

    shopping_list.append((product, quantity, price))

    total_cost += price

    continue_shopping = input("Wilt u nog een product aankopen? (ja/nee):").strip().lower()
    if continue_shopping != 'ja':
        break


print ("\nBoodschappenlijst:")
print ("------------------")


for item in shopping_list:
    product, quantity, price = item
    print(f"   - {product} {quantity}\t\t\t{price}")

print(f"\ntotal cost: \t\t\t{total_cost} ")