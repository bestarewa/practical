#!usr/bin/env python3
'''
__author__ = 'abba y abdullahi,abbaayabdullahi68@gmail.com'
'''

def derivative(f, h):
    """ Approximates the derivative of function f
given an h value. The closer h is to zero,
the better the estimate. """
    return lambda x: (f(x + h) - f(x)) / h

def fun(x):
    return 6*x


h = 0.0000001

der = derivative(fun, h)

x = 5.0
print('------------------------------------------------------')
print('                                  Approx.     Actual'  )
print('   x     f(x)    h   f\'(x)            f\'(x)'        )
print('------------------------------------------------------')
while x < 5.1:
    print('{:.5f} {:.5f} {:.8f}  {:.5f} {:.5f}'.format(x, fun(x), h, der(x), ans(x)))
    x += 0.01
