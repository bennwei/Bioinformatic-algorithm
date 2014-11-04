# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 00:24:48 2014

@author: Eric Liao
Hamming Distance Problem: Compute the Hamming distance between two strings.
     Input: Two strings of equal length.
     Output: The Hamming distance between these strings.

CODE CHALLENGE: Solve the Hamming Distance Problem.
 Sample Input:

GGGCCGTTGGT
GGACCGTTGAC

Sample Output:

3
"""
def mismatch(dna1, dna2):
    count = 0
    for n, i in zip(dna1, dna2):
       if n != i:
           count += 1
    return count
    
