def prime(x):
    a=0
    for i in range(2,x):
        if x%i==0:
            a = a+1
        i = i+1
    if a==0:
        print(str(x)+" is indeed a prime. ")
    else:
        print(str(x)+" is not a prime.")

prime(2)
prime(5)
prime(11)
prime(99)
prime(777)
