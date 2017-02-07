# Program to print out the divisors of a given number
a = []
number = int(input('Please enter a number: '))
for i in range(1,number):
    if number%i == 0:
        a.append(i)
print("The divisors of "+str(number)+" are: ")
print(a)
