a = [1,1,2,3,5,8,13,21,34,55,89]
b = []

#Scenario1
for i in a:
    if i<5:
        print(i)
#---------------
#Scenario2
for i in a:
    if i<5:
        b.append(i)
print(b)
#---------------
#Scenario3
b = [x for x in a if x<5]
print(b)
#---------------
#Scenario4        
num = int(input("Enter a number: "))
b = [x for x in a if x<num]
print(b)
