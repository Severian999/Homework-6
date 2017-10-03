# -*- coding: utf-8 -*-
"""
@author: Don Gass
"""

def desplode_time(years, days, hours, minutes, seconds):
    return (years * 31536000) + (days * 86400) + (hours * 3600) + (minutes * 60) + seconds

print(desplode_time(50, 300, 20, 50, 20))
print('50 years, 300 days, 20 hours, 50 mintues, and 20 seconds is', end=" ")
print(desplode_time(50, 300, 20, 50, 20), 'total seconds.')