def FrequentWords2(DNA, k):
    kmers = {} 
    for i in range (0, len(DNA)-k):
        kmer = DNA[i:i+k]
        if kmers.has_key(kmer):
            kmers[kmer] += 1
        else: 
            kmers[kmer] = 1
    for kmer, count in kmers.items():
        print kmer + "\t" + str(count)
        maxx = max(kmers.values())
        keys = [x for x,y in kmers.items() if y ==maxx]
    print keys, "the count is " + str(maxx)
        
    
    