prime_nums = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
num = 0

print(prime_nums)
print(len(prime_nums))

print("het 5de getal is " + str(prime_nums[4]))

prime_nums[24] = prime_nums[2]
prime_nums[2] = 97
print(prime_nums)

prime_nums.sort()
print(prime_nums)

for num in prime_nums:
    print (num)

prime_nums.sort(reverse = True)
print(prime_nums)

nummer = "97"
prime_nums = []
while nummer != "":
    prime_nums.append(int(nummer))
    nummer = input("geef een getal in (enter om te stoppen): ")

prime_nums.sort()
print(prime_nums)
