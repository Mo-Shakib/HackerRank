# https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=false

from math import gcd

# LCM - Least common multiple
# GCD - Greatest common divisor

def lcm(numbers):
    lcm_res = 1
    for i in numbers:
        lcm_res = lcm_res * i // gcd(lcm_res, i)
    return lcm_res

def getTotalX(a, b):
    x = lcm(a)
    z = lcm(a)
    y = gcd(*b)
    
    res = 0
    while x <= y:
        if y % x == 0:
            res += 1
        x += z
    return res