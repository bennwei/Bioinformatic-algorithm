# -*- coding: utf-8 -*-
def frequentWord_mismatch_with_comp(dna, k, d):
    '''
    Frequent Words with Mismatches and Reverse Complements Problem: Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.
      Input: A DNA string Text as well as integers k and d.
      Output: All k-mers Pattern maximizing the sum Countd(Text, Pattern)+ Countd(Text, Pattern)
      over all possible k-mers.

CODE CHALLENGE: Solve the Frequent Words with Mismatches and Reverse Complements Problem.

Sample Input:
     ACGTTGCATGTCGCATGATGCATGAGAGCT
     4 1

Sample Output:
     ATGT ACAT
     '''
    kmer_counts = { }
    most_frequent_kmers = [ ]
    for i in range(len(dna)-k+1):
         kmer = dna[i:i+k]
         kmer_comp = ReverseComplement(kmer)
         if kmer not in kmer_counts:
            kmer_counts[kmer] = len(approx_Pattern_Positions(dna, kmer, d))
            kmer_counts[kmer] += len(approx_Pattern_Positions(dna, kmer_comp, d))
            kmer_counts[kmer_comp] = kmer_counts[kmer]
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

def ReverseComplement(seq):
    base_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    bases = list(seq)
    for base in bases:
        if base not in 'ATCGatcg':
            print "Error: Not a DNA sequence!"
            return None
    return "".join([base_dict[base] for base in reversed(bases)])