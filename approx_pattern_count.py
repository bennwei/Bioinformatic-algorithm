# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 23:05:50 2014

@author: Eric Liao
"""

def approx_Pattern_Count(dna, pattern, d):
    """
	Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
	   Input: Two strings Pattern and Text along with an integer d.
	   Output: Count All positions where Pattern appears in Text with at most d mismatches.
	   Sample Input: 
	       TTTAGAGCCTTCAGAGG
	       GAGG
               2
           Sample Output:
               4
	"""
    count = 0
    for i in range(len(dna)-len(pattern)+1):
        pattern_2 = dna[i: i+len(pattern)]
        if mismatch(pattern, pattern_2) <= d:
            count += 1
    return count
def mismatch(pattern, pattern_2):
    """
	Compare two patterns and calculate edit distance - the number of mismatches between the sequences
	"""
    mismatch = 0
    for n, i in zip(pattern, pattern_2):
        if n != i:
           mismatch += 1
    return mismatch

with open('data/textbook/rosalind_1e.txt') as input_data:
	dna = input_data.read().strip()
