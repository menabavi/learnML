## lists, stirngs: problem 9

a = ["x", "y", "z"]
b = [4, 5, 6]

c = a + b
print(c)


## lists, stirngs: problem 10
def concatlist(l1, l2):
    return [sub[item] for item in (range(len(l2))) for sub in [l1, l2]]


l1 = [9, 6, 3]
l2 = ["us", "me", "we"]
l1.sort()
print(concatlist(l1, l2))
print(l1)

## lists, stirngs: problem 12


def rotator(test_list, n):
    test_list = [test_list[(i + n) % len(test_list)] for i, x in enumerate(test_list)]

    return test_list


list = [1, 2, 3, 4, 5, 6, 7]
n = 1
print(rotator(list, n))

## intermediate: problem 1

from itertools import product

for p in product(("+", "-", ""), repeat=8):
    print(p)
    s = "%s".join("123456789") % p
    if eval(s) == 100:
        print(s)
