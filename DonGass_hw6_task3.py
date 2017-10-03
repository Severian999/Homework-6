# -*- coding: utf-8 -*-
"""
@author: Don Gass
"""
def barsRedeemed( coupons ):
    bars = 0
    while coupons >= 10:
        bars, coupons = bars + 1, coupons - 9
    return bars

def bars( money ):
    return money + barsRedeemed( money )

#main
money = int(input('Enter an amount of money in dollars '))
print('For %d dollars, one can have %d bars' % (money, bars(money)))
