def ReverseComplement(seq):
    base_dict = {'a':'t', 'c':'g', 't':'a', 'g':'c', 'u':'a', 'A':'T', 'C':'G', 'T':'A', 'G':'C', 'U':'A'}
    bases = list(seq)
    for base in bases:
        if base not in 'ATCGatcg':
            print "Error: Not a DNA sequence!"
            return None
    return "".join([base_dict[base] for base in reversed(bases)])