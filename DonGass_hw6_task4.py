# -*- coding: utf-8 -*-
"""
@author: Don Gass
"""
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

#automated tests
for x in range(80, 86):
    for y in range(15, 22):
        print('The gcd of %d and %d is %d' % (x, y, gcd(x, y)))