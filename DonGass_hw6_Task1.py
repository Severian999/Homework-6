# -*- coding: utf-8 -*-
"""
@author: Don Gass
"""

def explode_seconds(seconds):
    years, secsr = divmod(seconds, 31536000)
    days, secsr = divmod(secsr, 86400)
    hours, secsr = divmod(secsr, 3600)
    minutes, secsr = divmod(secsr, 60)
    return (years, days, hours, minutes, secsr)

print(explode_seconds(1000000000000))
exploded = explode_seconds(1000000000000)
print('1 trillion seconds is %d years, %d days, %d hours, %d minutes, and %d seconds' \
      % (exploded[0], exploded[1], exploded[2], exploded[3], exploded[4]))
