import random

s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(){}|\;:<>,.?/"

passlen = int(input("How many characters would you like in your password?: "))


print("Your password is: ")
print("".join(random.sample(s,passlen)))
