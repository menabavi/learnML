from itertools import product

for p in product(("+", "-", ""), repeat=8):
    # print(p)
    s = "%s".join("123456789") % p
    if eval(s) == 100:
        print(s)
