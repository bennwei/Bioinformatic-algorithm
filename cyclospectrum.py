# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 00:12:59 2014

@author: Eric Liao
"""
MW_table = {}
with open('integer_mass_table.txt') as f:
    for line in f:
        file = line.split()
        MW_table[file[0]] = file[1]
       

def cyclospectrum(peptide):
    # Initialize as the mass 0 and the mass of the entire peptide.
    cyclospec = [0]
    # Find the masses of the all subpeptides
    L = len(peptide)
    subpeptide_ls = [peptide]
    peptide_loop = peptide + peptide
    for start in range(0, L):
        for length in range(1, L):
            subpeptide_ls.append((peptide_loop[start:start+length]))
    
    for subpeptide in subpeptide_ls:
       
        cyclospec += [sum([int(MW_table[amino_acid]) for amino_acid in subpeptide])]
        cyclospec_sorted = map(str,sorted(cyclospec))
    print ' '.join(cyclospec_sorted)


    



    