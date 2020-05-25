# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:07:40 2020

@author: A621587
"""
import math

ab = int(input())
#ab=10

bc = int(input())
#bc=10

ac = math.sqrt(ab**2+bc**2)
mc = ac/2

ab=ab/2
th = math.asin(ab/mc)
th = round(math.degrees(th))
print(str(th)+"°")
