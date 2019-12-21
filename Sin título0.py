# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 08:49:34 2019

@author: CEC
"""
"""
def to_upper_case(s):
    return str(s).upper()

def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('')
    
map_iterator = map(to_upper_case, 'abc')
print(type(map_iterator))
print_iterator(map_iterator)

map_iterator = map(to_upper_case, ['x', 'a', 'abc'])
print_iterator(map_iterator)

list_numbers = [1, 2, 3, 4]
map_iterator = map(lambda x: x * 2, list_numbers)
print_iterator(map_iterator)
"""
"""
test = zip()

# referring a zip class
print('The type of an empty zip : ', type(test))

list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
list2 = ['one', 'two', 'three', 'six']

test = list(zip(list1, list2))  # zip the values

 
print(test)

"""

floor_types = ['Parking', 'Shops', 'Food Court', 'Offices']
floors_numbers = range(-1,3)
elevator_dict = dict(zip(floor_types, floors_numbers))
print(elevator_dict[:-1])
