#!/usr/bin/python3

import math, decimal

# Demonstrate Integers

x, y, z = 1, 2, 3

print(x, y, z)

def boolEx(a, b):
    print(type(a))
    print(a and b)
    print(a or b)
    print(not b)
    d = (1 > 2)
    print(d)
    e = ((2 > 1) and (3 <= 3))
    print(e)
    
boolEx(True, False)


def intEx():
    # integers, binary, octal, hexadecimal
    x = 5
    y = 2

    print("x + y = ", x+y)

    print("{} + {} = ".format(x, y), x+y)
    print("{} - {} = ".format(x, y), x-y)
    print("{} * {} = ".format(x, y), x*y)
    print("{} / {} = ".format(x, y), x/y)
    print("{} % {} = ".format(x, y), x%y)
    print("{} ** {} = ".format(x, y), x**y)

    print("Binary format for 4", bin(4))    
    print("Hexidecimal format for 4", hex(4))

    print(float(x))
    print(pow(x,y))

    z = 100/3 # division problem assigned to 'z'
    print(z) # answer 'z'
    print(type(z)) # type of 'z'

    print(round(z,3)) # round to nearest whole

    print(math.ceil(z)) # round up
    print(math.floor(z)) # round down
    
    z = decimal.Decimal("1.234567891011121314")
    print(z)
    
intEx()
