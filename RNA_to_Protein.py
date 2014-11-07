def RNA_to_Protein(RNA_file, codon_table_file):
     """
     Protein Translation Problem: Translate an RNA string into an amino acid string.
     Input: An RNA string Pattern and the array GeneticCode.
     Output: The translation of Pattern into an amino acid string Peptide.
     >>>RNA_to_Protein('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA')
     MAMAPRTEINSTRING
     """
     RNA_seq = open(RNA_file)
     RNA = RNA_seq.readline().strip()
     codon_table = {}
     with open(codon_table_file) as f:
         for line in f:
             if " \n" in line:
                 triplet = line.strip()
                 codon_table[triplet] = "stop"
             else:
                 (triplet, aa) = line.strip().split(" ")
                 codon_table[triplet] = aa
     protein = ' '
     for i in xrange(0, len(RNA)-2, 3):
         codon = RNA[i:i+3]
         if codon_table[codon] != "stop":
             protein += codon_table[codon]
         else:
             break
     print protein
        
    
             