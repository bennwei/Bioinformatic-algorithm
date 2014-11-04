# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 22:34:14 2014

@author: Eric Liao
"""
with open('dataset_9_4.txt') as input_data:
    pattern, dna, d = [line.strip() if index != 2 else int(line.strip()) for index, line in enumerate(input_data.readlines())]
approx_match = []
for i in range(len(dna)-len(pattern)+1):
    mis_match = 0
    for j in range(len(pattern)):
        if dna[i:i+len(pattern)][j] != pattern[j]:
            mis_match += 1 
    if mis_match <= d:
        approx_match.append(str(i))
print (' '.join(approx_match))

with open('dataset_9_4_output.txt', 'w') as output_data:
    output_data.write(' '.join(approx_match))


            