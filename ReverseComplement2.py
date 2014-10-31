def ReverseComplement(seq):
    base_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    bases = list(seq)
    for base in bases:
        if base not in 'ATCGatcg':
            print "Error: Not a DNA sequence!"
            return None
    return "".join([base_dict[base] for base in reversed(bases)])