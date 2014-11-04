def miniSkew(seq):
    '''
Minimum Skew Problem: Find a position in a genome minimizing the skew.
     Input: A DNA string Genome.
     Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).
 
CODE CHALLENGE: Solve the Minimum Skew Problem.
Sample Input:
     TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT
 
Sample Output:
     11 24
 
 
'''
    skew_value = 0
    min_skew = 0
    
    for index, n in enumerate (seq):
        # Determine the skew value based on rules above.
        if n == 'C': 
            skew_value += 1
        elif n == 'G':
            skew_value -= 1
        