a = int(input('Enter a number for God\'s sake '))

if a%2 == 0:
    print('Yo, it\'s even..')
else:
    print('It is odd like you')


if a%4==0:
    print('Jackpot! It is a multiple of 4 too!')


print('Now, prepare to enter two numbers')
num = int(input('The first number: '))
check = int(input('The second number: '))

if num%check == 0:
    print(str(check)+' divides evenly into '+str(num))
else:
    print('Cool story..')
