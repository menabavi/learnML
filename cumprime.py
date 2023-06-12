n = int(input("please enter a number:"))
x = []


def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for i in range(1, n + 1):
    if isprime(i):
        x.append(i)


print("The prime numbers up to {} are:".format(n), x)
