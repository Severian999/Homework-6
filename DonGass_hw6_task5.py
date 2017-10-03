# -*- coding: utf-8 -*-
"""
@author: Don Gass
"""
def decValue(bit_list):
    if not bit_list:
        return 0
    else:
        dval = 0
        for i in range(len(bit_list)):
            dval = dval + bit_list.pop(0) * (2 ** len(bit_list))
        return dval

#test cases
print('Automated test cases')

my_bin = [1,0,1,1]
print('The binary list', my_bin, end=' ')
print('is equal to %d' % decValue(my_bin))

my_bin = [1,1,1,0,0,1,0,1]
print('The binary list', my_bin, end=' ')
print('is equal to %d' % decValue(my_bin))

my_bin = [1,0,0,0,0,1,0,1]
print('The binary list', my_bin, end=' ')
print('is equal to %d' % decValue(my_bin))

my_bin = [1]
print('The binary list', my_bin, end=' ')
print('is equal to %d' % decValue(my_bin))

my_bin = [1,0]
print('The binary list', my_bin, end=' ')
print('is equal to %d' % decValue(my_bin))

my_bin = [1,1,1,0,1]
print('The binary list', my_bin, end=' ')
print('is equal to %d' % decValue(my_bin))

my_bin = [1,0,1,0,1,0,1,0,1,0,1]
print('The binary list', my_bin, end=' ')
print('is equal to %d' % decValue(my_bin))
