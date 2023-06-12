list = ["+", "-", ""]
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
l1 = ()
l2 = ()
operate = ()
comb = ()
string = ""
comb_str = ()
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                for m in range(3):
                    for n in range(3):
                        for o in range(3):
                            for p in range(3):
                                l1 += (
                                    list[i],
                                    list[j],
                                    list[k],
                                    list[l],
                                    list[m],
                                    list[n],
                                    list[o],
                                    list[p],
                                )
                                operate += (l1,)
                                l1 = tuple()

# print(operate)

for f in range(len(operate)):
    for e in range(len(digits)):
        l2 += digits[e], operate[f][e - 1]
    comb += (l2,)
    l2 = tuple()

# for q, y in enumerate(comb):
#    y = y[q - 1][:-1]
print(comb)

# comb_str = "".join(comb[0])
# print(comb_str)

# for a in range(len(comb)):
#    string = "".join(comb[a - 1])
#   comb_str += (string,)
#  del string
# for a in range(len(comb_str)):
#   if eval(comb_str[a][:-1]) == 100:
#      print(comb_str)
# print(comb_str)

if type(comb_str) is list:
    print("a list")
elif type(comb_str) is tuple:
    print("a tuple")

temp = list(comb_str)
# if eval(str(comb[a])) == 100:
#   print(comb[a])

# print(comb)
