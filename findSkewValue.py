def findSkewValue(dna):
    '''Give all values of Skewi (GAGCCACCGCGATA) for i ranging from 0 to 14,
    start with 0 from a DNA sequence, if nucleotide is G, then +1; if C, then  -1.Otherwise, A and T
    no change in value.  
    >>>findSkewValue("CATGGGCATCGGCCATACGCC")
    0 1 1 2 1 0 0 -1 -2 -1 -2 -1 -1 -1 -1
    '''
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
        
    
    print ' '.join(str(i) for i in skew_list)
    
             
    