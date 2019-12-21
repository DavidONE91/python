# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:23:48 2019

@author: CEC

#ENTEROS

ac1Num= int(input("What is the IPV4 ACL number? "))
if ac1Num>= 1 and ac1Num<=99:
    print("This is a standard IPV4 ACL. ")
elif ac1Num >= 100 and ac1Num <=199:
    print("This is a extended IPV4 ACL. ")
else:
        print ("This is not a standard or extension IPV4 ACL. ")
      
#FOR
devices= ["R1","R2","R3","S1","S2"]
for item in devices:
    print(item)


devices= ["R1","R2","R3","S1","S2"]
for item in devices:
    if "R" in item:
        print(item)   
 
#append agrega valores
devices= ["R1","R2","R3","S1","S2"]
switches=[]
for item in devices:
    if "S" in item:
        switches.append(item)
print(switches)

x=input("Enter a number to count to: ")
x=int(x)
y=1
while y<=x:
    print(y)
    y=y+1

#Romper lazo infinito
x=input("Enter a number to count to: ")
x=int(x)
y=1
while True:
    print(y)
    y=y+1
    if y>x:
        break

while True: 
  x=input("Enter a number to count to: ")
 # x=str(x)
  
  if x == 'q' or x == 'quit':
      break
  x=int(x)
  y=1
  while True:
      print(y)
      y=y+1
      if y>x:
          break

##
for i in range(3):
    print(i)    
    
##    
    
result=0
n=5
for i in range(1,n+1):
    result +=i
print(result)  ##mucho ojo con la identación, puede provocar errores


## 
for i in range(10,0,-2):
    print(i)

#FUNCIONES
def message():
    print("Hola")
    
print("Start")
message()


#
def hiAll(name1,name2):
    print("Hola",name1)
    print("Hola",name2)

hiAll("Greg","David")



#
def address(street, city, postalCode):
    print("Your address is:", street,"St.,",city, postalCode)
    
s = input("Street: ")
pC = input("Postal Code: ")
c = input("City: ")

address(s,c,pC)


#
def subtra(a, b):
    print(a - b)
    
subtra(a=5, b=2)
subtra(b=2, a=5)

#
def subtra(a, b):
    print(a - b)
    
subtra(5, b=2)
subtra(5, 2) #subtra(a=5, 2) sale error porque no se puede definir una variable al inicio sino solo al final como en la linea anterior


#
def multiply(a, b):
    return a * b

print(multiply(3, 4))

def multiply (a,b):
    return

print(multiply(3, 4))

def wishes():
    return "Happy birthday"


#
def hiEverybody(myList):
    for name in myList:
        print("Hi,", name)
        
hiEverybody(["Adam", "Jhon", "Carlos", "Ana"])

# 
def createList(n):
    myList = []
    for i in range(n):
        myList.append(i)
    return myList

print(createList(5))


# 
def a(x, y):
    return x + y
"""
b= lambda x, y: x + y
print(b(5,2))
