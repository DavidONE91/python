# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 08:11:56 2019

@author: CEC
"""

def readint(prompt, min, max):
    try:
        number=int(input(prompt))
        if number >= min and number <= max:
          #  print ("The number is", number)
          assert number < min or number > max:
          return number        
        
            print ("Error: the value is not within permitted range (",min,",",max,")")
            
    except ValueError:
        print("Error: wrong input")

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
