# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 08:11:12 2019

@author: CEC
"""

"""
sumar = lambda x, y: x + y
print(sumar(5,2))
"""

"""
revertir=lambda cadena: cadena[::-1] #[::-1]transpuesta
print(revertir("Hola"))
"""

"""
impar = lambda num : num%2 != 0
print(impar(5))
"""

"""
doblar = lambda num : num*2
print(doblar(2))
"""
"""
seq = ['data', 'salt', 'dairy','cat','dog']
print(list(filter(lambda word: word[0]=='d',seq)))
"""

#NumPrimo
#def isPrime(num):
num=int(input("Numero: "))
cont=0
for i in range(1,20):
    if (num%i)==0:
        cont+=1
if cont==2:
    print("El numero",num,"es primo")
#return num

       
#    isPrime(i+1):
#        print(i+1,end="")
        
#print()