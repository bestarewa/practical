#!usr/bin/env python3

'''
__author__ = 'abba y abdullahi , abbayabdullahi68@gmail.com'
'''

import turtle

def report_position(x, y):
    '''Simply prints the values of x and y.'''
    print("x =", x, " y =", y, flush=True)
    

turtle.onscreenclick(report_position)
turtle.mainloop()
