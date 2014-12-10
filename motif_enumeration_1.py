def motif_Enumeration(Dna, k, d):
    """
    Given a collection of strings Dna and an integer d, a k-mer is a (k,d)-motif if it appears in every string from Dna with at most d mismatches. 
    For example, the implanted 15-mer in the strings above represents a (15,4)-motif. Implanted Motif Problem: Find all (k, d)-motifs in a 
    collection of strings.
        Input: A collection of strings Dna, and integers k and d.
        Output: All (k, d)-motifs in Dna.
    """
    patterns = []
   
    for i in xrange(0, (len(Dna)+1-k)):
        kmers = Dna[i, i+k]
        for kmer in kmers:
            if mismatch(kmer, Dna_pattern) >= d:
                patterns.append(kmer)
        return set(patterns)

def mismatch(pattern, pattern_2):
    """
	Compare two patterns and calculate Hamming distance - the number of mismatches between the sequences
	"""
    mismatch = 0
    for n, i in zip(pattern, pattern_2):
        if n != i:
           mismatch += 1
    return mismatch