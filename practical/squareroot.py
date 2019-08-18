#/usr/bin/env python3
'''
__author__ = ' abba y abdullahi , abbayadullahi68@gmail.com'

'''

def square_root(val):
    """ Compute an approximation of the square root of x """
    root = 1.0
    diff = root*root -val
    while diff > 0.00000001 or diff < -0.00000001:
       root = (root + val/root) / 2
       diff = root*root -val

    return root



from math import sqrt

d = 1.0
while d <= 10.0:
    print('{0:6.1f}: {1:16.8f} {2:16.8f}'\.format(d,square_root(d),sqrt(d))) )
    d += 0.5

