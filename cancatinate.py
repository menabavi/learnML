## lists, stirngs: problem 10

a = ["x", "y", "z"]
b = [4, 5, 6]
c = []
for i in range(len(a)):
    c += (a[i], b[i])

print(c)

## lists, stirngs: problem 9
a = ["x", "y", "z"]
b = [4, 5, 6, 7, 99]
c = b
for i in range(len(a)):
    c += a[i]

print(c)


## lists, stirngs: problem 12

list = ["1", "2", "3", "4", "5", "6", "7"]
n = 3
list1 = []
for i in range(len(list)):
    list1 += list[(i + n) % len(list)]

print(list1)
