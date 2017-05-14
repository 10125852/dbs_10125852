# -*- coding: utf-8 -*-
"""
date: 13/05/2017
author: 10125852 InSun Ahn

"""

'''
CA05 Part B: Refactoring calculator using lambda, map, reduce, filter functions
'''

# Import math & numpy to use functions.
import numpy as np
import math

class Calculator(object):
    ''' class for 11 calculator functions to handle listed values.'''
  
    # Add all elements in a list and return the total.
    def sum(self, values):
        return reduce(lambda x, y: x + y, values)
   
    # Return the sum of values in two lists.
    def add(self, list1, list2):
        return map(lambda x, y: x + y, list1, list2)
    
    # Multiply all elements in a list.
    def multiply(self, values):
        return reduce(lambda x, y: x * y, values)
    
    # Return the maximum value in a list.
    def max(self, values):
        return reduce(lambda x, y: x if (x>y) else y, values)
    
    # Return the minimum value in a list.
    def min(self, values):
        return reduce(lambda x, y: x if (x<y) else y, values)
    
    # Return only even numbers among the listed values.
    def is_even(self, values):
        return filter(lambda x: x % 2 == 0, values)
    
    # Return only odd numbers among listed values.
    def is_odd(self, values):
        return filter(lambda x: x % 2 == 1, values)
    
    # Get average of the values in a list for the below above/below mean functions.
    def mean(self, values):
        return np.mean(values)
        
    # Filter the values that are above mean in a list.
    def above_mean(self, values, mean):
        return filter(lambda x: x > mean, values)
    
    # Filter the values that are below mean in a list.
    def below_mean(self, values, mean):
        return filter(lambda x: x < mean, values)    
    
    # Get squared values of each element in a list.
    def squared(self, values):
        return map(lambda x: x ** 2, values)
    
    # Get square root of each element in a list 
    def sqrt(self, values):
        return map(lambda x: math.sqrt(x), values)
    
    
myCal = Calculator()

# Give varibles for two sample lists
a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Excute calculations for the above lists.
print myCal.add(a,b)
print myCal.sum(a)
print myCal.is_even(a)
print myCal.is_odd(b)
print myCal.max(a)
print myCal.min(a)
print myCal.multiply(a)
print myCal.mean(a)
print myCal.mean(b)
print myCal.above_mean(a, myCal.mean(a))
print myCal.below_mean(b, myCal.mean(b))
print myCal.squared(a)
print myCal.sqrt(a)
