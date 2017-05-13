# -*- coding: utf-8 -*-
"""
date: 13/05/2017
author: 10125852 InSun Ahn

"""

'''
CA05 Part B: Refactoring calculator using lambda, map, reduce, filter functions
'''

import math

class calculator(object):
    ''' class for 10 calculator functions to handle listed values.'''
  
    # Add all elements in a list and return the total.
    def add(self, values):
        return reduce(lambda x, y: x + y, self.values)
   
    # Return the sum of values in two lists.
    def sum(self, list1, list2):
        return map(lambda x, y: x + y, self.list1 + self.list2)
    
    # Return the maximum value in a list.
    def max(self, values):
        return reduce(lambda x, y: x if (x>y) else y, self.values)
    
    # Return the minimum value in a list.
    def min(self, values):
        return reduce(lambda x, y: x if (x<y) else y, self.values)
    
    # Return only even numbers among the listed values.
    def is_even(self, values):
        return filter(lambda x: x % 2 == 0, self.values)
    
    # Return only odd numbers among listed values.
    def is_odd(self, values):
        return filter(lambda x: x % 2 == 1, self.values)
    
    # Return the values that are above mean in a list.
    def above_mean(self, values, mean):
        return filter(lambda x: x > mean, values)
    
    # Return the values that are below mean in a list.
    def below_mean(self, values, mean):
        return filter(lambda x: x < mean, values)    
    

        