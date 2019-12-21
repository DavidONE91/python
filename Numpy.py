# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:08:42 2019

@author: CEC
"""

import numpy as np
"""
a=np.array([1,2,3])
print(a)


b=np.array([(1,2,3),(4,5,6)])
print(b)

array=np.array([[1,2,3,4],[5,6,7,8]], dtype=np.int64)
print(array)
"""
"""
unos=np.ones((3,4))
print(unos)

ceros=np.zeros((3,4))
print(ceros)
"""
"""
a=np.array([(8,9,10),(11,12,13)])
print(a)
print("\n"*2)
a=a.reshape(3,2)
print(a)

a=np.array([(1,2,3,4),(3,4,5,6)])
print(a)
print("\n"*1)
print(a[1,3])

a=np.array([(1,2,3,4),(3,4,5,6)])
print(a[0:,1])

"""
"""
a=np.array([2,4,8])
print(a.min())
print(a.max())
print(a.sum())

a=np.array([(1,2,3),(3,4,5)])
print("\n"*2)
print(np.sqrt(a))
print("\n"*2)
print(np.std(a))
"""

x=np.array([(1,2,3),(3,4,5)])
y=np.array([(1,2,3),(3,4,5)])
print(x+y)
print("\n")
print(x-y)
print("\n")
print(x*y)
print("\n")
print(x/y)

a=np.array([(1,2),(3,4)])
b=np.array([(1,2),(3,4)])
print("\n"*2)
print(np.dot(a,b))