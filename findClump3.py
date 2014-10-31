from collections import defaultdict

def findClump(seq, k, L, t):
    """Given integers L and t, a string Pattern forms an (L, t)-clump inside a (larger) string Genome 
    if there is an interval of Genome of length L in which Pattern appears at least t times. For example, 
    >>> findClump('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGAC
                    TCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA', 5,50, 4)
    [CGACA, GAAGA]
    Clump Finding Problem: Find patterns forming clumps in a string.
     Input: A string Genome, and integers k, L, and t.
     Output: All distinct k-mers forming (L, t)-clumps in Genome.
    """
    lookup = defaultdict(list)
    result =set()
    
    for i in range((len(seq) - k +1)):
        kmer = seq[i : i + k]
        
        while lookup[kmer] and i+k - lookup[kmer][0] >L:
            lookup[seq].pop(0)
        
        lookup[kmer].append(i)
        if len(lookup[kmer]) == t:
            result.add(kmer)
    return result

