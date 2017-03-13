def Fib(x):
    a=[1,1]
    i=2
    if x==0:
        print('Funny guy..')
    elif x==1:
        print(a[0])
    elif x==2:
        print(a)
    else:
        while(i<x):
            a.append(a[-1]+a[-2])
            i=i+1
        print(a)
#Fib(5)
#Fib(10)
#Fib(2)
#Fib(0)
x =int(input('Enter number of digits : '))
Fib(x)
