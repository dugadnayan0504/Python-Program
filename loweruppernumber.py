import re
evn = []
odd = []


def even_odd(n4):
    for i in n4:
        if i % 2 == 0:
            evn.append(i)
        else:
            odd.append(i)


st = input()
n1 = "".join(re.split("[^a-z]*", st))
n1.split()
n2 = "".join(re.split("[^A-Z]*", st))
n2.split()
n3 = "".join(re.split("[^0-9]*", st))
n3.split()

n4 = [int(x) for x in n3]

even_odd(n4)

n1 = sorted(n1, key=str.lower)
n2 = sorted(n2, key=str.upper)
result = n1 + n2 + odd + evn

for i in result:
    print(i, end="")
