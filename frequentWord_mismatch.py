# -*- coding: utf-8 -*-
def frequentWord_mismatch(dna, k, d):
    '''
    Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
     Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
     Output: All most frequent k-mers with up to d mismatches in Text.

    CODE CHALLENGE: Solve the Frequent Words with Mismatches Problem.

    Sample Input:
        ACGTTGCATGTCGCATGATGCATGAGAGCT
        4 1

    Sample Output:
    GATG ATGC ATGT
     '''
    kmer_counts = { }
    most_frequent_kmers = [ ]
    for i in range(len(dna)-k+1):
         kmer = dna[i:i+k]
         if kmer not in kmer_counts:
            kmer_counts[kmer] = len(approx_Pattern_Positions(dna, kmer, d))
    max_count = max(kmer_counts.values())        
    for kmer, count in kmer_counts.items():
        if count == max_count:
            most_frequent_kmers.append(kmer)
    print ' '.join(most_frequent_kmers)

def approx_Pattern_Positions(dna, pattern, d):
    """
	Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
	   Input: Two strings Pattern and Text along with an integer d.
	   Output: All positions where Pattern appears in Text with at most d mismatches.
	   
             
	"""
    
    pattern_positions = []
    for i in range(len(dna)-len(pattern)+1):
        pattern_2 = dna[i: i+len(pattern)]
        if mismatch(pattern, pattern_2) <= d:
            pattern_positions.append(str(i))
    return pattern_positions
    
def mismatch(pattern, pattern_2):
    """
	Compare two patterns and calculate Hamming distance - the number of mismatches between the sequences
	"""
    mismatch = 0
    for n, i in zip(pattern, pattern_2):
        if n != i:
           mismatch += 1
    return mismatch
