import time
start_time = time.time()
in_file = open('findClump_example.txt','r')
ou_file = open('data_set_out.txt', 'w')
        
def findClump(seq, k, L, t):
        """Generate the indices of the (possibly overlapping) occurrences of
    pattern in text. For example:

    >>> findClump(5, 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGAC\n
                    TCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA', 50, 4)
    [CGACA, GAAGA]

    """
        kmer_len = k
        list = []
        n= 0 
        n += 1
        kmer_dict = {}
        for i in range(len(seq) - kmer_len):
            kmer = seq[i : i +kmer_len]
            if kmer in kmer_dict:
                kmer_dict[kmer][0] += 1
                kmer_dict[kmer].append(i)
            else: 
                kmer_dict[kmer] = [1, i]
    
        for kmer in kmer_dict:         
            # look for kmer repeated t times with an index distance of L
            if kmer_dict[kmer][0] >= t and kmer not in list:
                for n in range(len(kmer_dict[kmer]) - t):
                    if kmer_dict[kmer][n+t-1] - kmer_dict[kmer][n] <= L:
                        if kmer not in list:
                            list.append(kmer)
        for kmer in list: 
            print (kmer),
        
print(str(time.time() - start_time) + ' seconds\n')