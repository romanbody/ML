#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:47:19 2019

@author: romanbody
"""

text_data =["  test test by .mac os",
            " python is .greate language",
            " also used with ML algorithms"]

strip_whitespaces = [string.strip() for string in text_data]
remove_periods = [string.replace(".","") for string in strip_whitespaces]

print (text_data)

print (strip_whitespaces)

print (remove_periods)

pokus = 1
print (remove_periods.count("sdsdfg sdfg "))