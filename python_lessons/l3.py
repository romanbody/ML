# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:01:10 2020

@author: A621587
"""

# number of input numbers and number of numbers in A and B
n, m = input().split() 

# input list of numbers
sc_ar = input().split()

# happy numbers 
A = set(input().split())

# unhappy numbers 
B = set(input().split())


print(sum([(i in A) - (i in B) for i in sc_ar]))