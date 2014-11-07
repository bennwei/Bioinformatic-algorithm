# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 23:59:42 2014

@author: Eric Liao
"""
def subpeptide(peptide):
    """
     For example, the cyclic peptide NQEL has 12 subpeptides: N, Q, E, L, NQ, QE, EL, LN, NQE, QEL, ELN, and LNQ. 
     We will also assume that subpeptides may occur more than once if an amino acid occurs multiple times in the peptide 
     (e.g., ELEL also has 12 subpeptides: E, L, E, L, EL, LE, EL, LE, ELE, LEL, ELE, and LEL.
    """
    L = len(peptide)
    ls = []
    peptide_loop = peptide + peptide
    for start in range(0, L):
        for length in range(1, L):
            ls.append((peptide_loop[start:start+length]))
    return ls
            
