n = int(input("please enter a number:"))
isprime = True

for i in range(2, n):
    if n % i == 0:
        isprime = False
        break

if isprime:
    print("th umber is prime"),
else:
    print("the number is not prime")
