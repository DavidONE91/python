# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:43:06 2019

@author: CEC
"""

#devices=[]
file=open("devices.txt","a")

##    print(item)

while True:
    newItem=input("Insert New device:")
    if newItem == "exit":
        print("All done")
        break
    #else:
    file.write(newItem + "\n")

#for item in file:
#    item=item.strip()
#    devices.append(item)
    
file.close()
#print(devices)