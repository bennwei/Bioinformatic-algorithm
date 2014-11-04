# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 00:07:24 2014

@author: Eric Liao
"""

with open('dataset_7_6.txt') as input_data:
    dna = input_data.read().strip()
skew_value, min_skew, min_ind = 0, 1, []
for index, nucleotide in enumerate(dna):
# Determine the skew value.
    if nucleotide == 'C':
        skew_value -= 1
    elif nucleotide == 'G':
        skew_value += 1
# Check if it matches the current minimum, or is a new minimum.
    if skew_value == min_skew:
        min_ind.append(str(index+1))
    elif skew_value < min_skew:
        min_skew = skew_value
        min_ind = [str(index+1)]
print (' '.join(min_ind))

with open('dataset_7_6.txt', 'w') as output_data:
    output_data.write(' '.join(min_ind))