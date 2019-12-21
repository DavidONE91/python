# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 09:05:14 2019

@author: CEC

def isPrime(num):
for i in range(1,20):
    if (num%i)==0:
        cont+=1
if cont==2:
    return True
elif cont!=2:
    return False
#    print("El numero",num,"es primo")

##Primo1
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for i in range(1,100):
    if isPrime(i+1):
        print(i+1,end=" ")
print()
"""
##Primo2
def is_prime(x):
    if x<2:
        return False
    elif x == 2:
        return True
    for n in range(2,x):
        if x % n == 0:
            return False
    return True

print(is_prime(5))

for i in range(1,100):
    if is_prime(i+1):
        print(i+1, end=" ")
        