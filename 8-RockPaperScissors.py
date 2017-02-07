print('Two player Rock, Paper, Scissors! ')
replay = 'y'
while(replay == 'y'):
    
    print('Your choices: ')
    print('Rock : 1')
    print('Paper: 2')
    print('Scissor: 3')

    p1wins = 'Player 1 wins!'
    p2wins = 'Player 2 wins!'
    p3 = 'Draw!'

    p1 =int(input('Player 1, go: '))
    p2 =int(input('Player 2, go: '))

    if p1==1:
        print(p1wins if p2==3 else p2wins)
    elif p1==2:
        print(p1wins if p2==1 else p2wins)
    elif p1==3:
        print(p1wins if p2==2 else p2wins)
    elif p1==p2:
        print(p3)

    replay = str(input('Would you like to continue(y/n)?: '))

        
