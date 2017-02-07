x = str(input('Enter the word to be checked: '))
if x == x[::-1]:
    print('It is a palindrome. ')
else:
    print('It\'s not a palindrome.')
