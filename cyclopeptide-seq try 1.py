def cyclopeptide_Sequecing(spectrum):
    MW_table = {'A': '71', 'C': '103', 'E': '129', 'D': '115', 'G': '57', 'F': '147', 'I': '113', 'H': '137', 'K': '128', 'M': '131', 'L': '113', 'N': '114', 'Q': '128', 'P': '97', 'S': '87', 'R': '156', 'T': '101', 'W': '186', 'V': '99', 'Y': '163'}
    peptides = []
    while peptides:
        temp_peptides_list = []
        temp_peptides_list.append([aa for aa in MW_table.keys()])
        for peptide in temp_peptides_list:
    
