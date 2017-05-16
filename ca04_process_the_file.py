# -*- coding: utf-8 -*-
"""
date: 02/05/2017
author: 10125852 InSun Ahn

"""

# Open the file.
myfile = "test_short.txt"

# Read the file by lines and strip the lines.
data = [line.strip() for line in open(myfile, 'r')]

# Print the number of lines.
print(len(data))

# Give a separater variable.
sep = 72*'-'

# Define class for commit

class commit(object):
    