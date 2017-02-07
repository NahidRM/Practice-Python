import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    for j in b:
        if i==j:
            c.append(i)
# print(c)
# Now for randomly generated lists
d = []
e = []
f = []
lenlist1 = random.randint(0,20)
lenlist2 = random.randint(0,20)
for i in range(1,lenlist1):
    i = random.randint(0,100)
    d.append(i)
for i in range(1,lenlist2):
    i = random.randint(0,100)
    e.append(i)
for i in d:
    for j in e:
        if i == j:
            f.append(i)
print(d)
print(e)
print('List overlap of controlled random generated lists: ')
print(f)
# One line command yet to be solved 
