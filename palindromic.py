import operator

sentence = str(input("please enter your text:"))
words = sentence.split()
palindoromic = {}


def reverse(txt):
    global palin
    palin = True
    if txt != txt[::-1]:
        palin = False
    # print(palin)
    return palin


for i, x in enumerate(words):
    reverse(x)
    if palin:
        palindoromic.update({x: len(x)})


max_palindro = max(palindoromic.items(), key=operator.itemgetter(1))[0]
print(max_palindro)
