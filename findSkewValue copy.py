# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 23:57:16 2014

@author: Eric Liao
"""

def findSkewValue(dna):
    skew_value = 0
    skew_list = []
    skew_list.append(0)
    for n in dna:
        if n == 'C':
            skew_value -= 1
            skew_list.append(skew_value)
        elif n == 'G':
            skew_value += 1
            skew_list.append(skew_value)
        else:
            skew_value += 0
            skew_list.append(skew_value)
    for i in skew_list:
        l = ' '.join(map(str, skew_list))
        return l