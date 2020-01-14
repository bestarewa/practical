#!usr/bin/env python3
'''
__author__ = 'abba y abdullahi'
'''
from math import sqrt,sin,cos,pi,radians


sx = int(float(input(' enter x coordinate of spacecraft:')))
sy = int(float(input(' enter y coordinate of spacecraft:')))
# this satellite is start with new (y,x) value to find the distanc

x = int(float(input(' enter  initial  satellite x coordinate:')))
y = int(float(input(' enter  initial  satellite x coordinate:')))

# let add radia  which i convert to it ti 60 degree
rads = radians(60)

cos_theta = cos(rads)
sin_theta = sin(rads)


# let make it complate revolution  (6*60 = 360 degrees)
for increment in range(0,7):
    dist = sqrt((sx-x)*(sx-y) +(sy-y)*(sy-y))
    print('Distance to satellite{0:10.2f} km'.format(dist))
    x ,y = x*cos_theta - y*sin_theta, x*sin_theta + y*cos_theta


