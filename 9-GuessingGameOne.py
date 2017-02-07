import random
again = True
guesses = 0
x = random.randint(1,9)
while(again !='exit'):
    user = int(input("Enter your guess: "))
    higher ="Too high"
    lower ="Too low"
    correct ="You're right"
    if x!=user:
        print(higher if user>x else lower)
        guesses = guesses+1
    else:
        print(correct)
        break
    again = input("Type exit if you wish to end, if not press enter: ")

if x==user:
    print("It took you "+str(guesses)+" guesses to get it right")
elif again=='exit':
    print("You quit after "+str(guesses)+ " attempts")

