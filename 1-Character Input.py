from datetime import date
name = input('Enter your name: ')
age = int(input('Enter your age: '))
print('You will be a 100 years old in the year: ' + str(date.today().year + (100-age)))
print('You will probably be dead by then anyway..')
