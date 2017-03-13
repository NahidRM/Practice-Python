import random

def compare(number, user):
    cowbull=[0,0]
    for i in range(len(number)):
        if number[i]==user[i]:
            cowbull[1]+=1
        elif user[i] in number:
            cowbull[0]+=1
    return cowbull

if __name__=="__main__":
    a="0123456789"
    number=random.sample(a,4)
    guess=0
    again=True
    while again:
        user=input("Enter your best guess: ")
        result=compare(number,user)
        guess+=1
        print("Your result: ")
        print("Cows:"+str(result[0])+" and Bulls: "+str(result[1]))
        repeat=input("Would you like to try again?(Y/N): ")
        if repeat=='N':
            again = False

    print("Total number of guesses: ")
    print(guess)
