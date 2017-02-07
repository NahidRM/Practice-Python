#Similar to my solution in Excercise 5, not precisely randomly generated
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
