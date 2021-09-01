import random
passlen=int(input("Enter the len of password"))
s="abcdefghijklmnopqurstuvwxyz0123456789ABCSEFGHIJKLMNOPQURSTUVWXYZ!@#$"
P="".join(random.sample(s,passlen))
print(P)