# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:14:08 2019

@author: CEC
"""
devices=[]
file=open("devices.txt","r")
for item in file:
    item=item.strip()
    devices.append(item)
#    print(item)
file.close()
print(devices)