


def DNA_to_RNA(DNA_file):
    """Return dna string as rna string.
    >>>DNA_to_RNA('CCGGAAGAGCTTACTTAG')
    'CCGGAAGAGCUUACUUAG' 
    """
    DNA_seq = open(DNA_file)
    DNA = DNA_seq.readline().strip()
    return DNA.replace('T', 'U')

def RNA_to_Protein(RNA, codon_table_file):
     """
     Protein Translation Problem: Translate an RNA string into an amino acid string.
     Input: An RNA string Pattern and the array GeneticCode.
     Output: The translation of Pattern into an amino acid string Peptide.
     >>>RNA_to_Protein('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA')
     MAMAPRTEINSTRING
     """
     
     codon_table = {}
     with open(codon_table_file) as f:
         for line in f:
             if " \n" in line:
                 triplet = line.strip()
                 codon_table[triplet] = "stop"
             else:
                 (triplet, aa) = line.strip().split(" ")
                 codon_table[triplet] = aa
             return codon_table
     protein = ' '
     for i in xrange(0, len(RNA)-2, 3):
         codon = RNA[i:i+3]
         if codon_table[codon] != "stop":
             protein += codon_table[codon]
         else:
             break
     return protein
    
def pattern_encoding_in_rna(RNA, peptide):
     pattern_encoding_peptide = [ ]
     for i in range(len(RNA) - 3*len(peptide) +1):
         sub_rna = RNA[i : i+3*len(peptide)]
         sub_peptide = RNA_to_Protein(RNA, codon_table)
         if sub_peptide == peptide:
             pattern_encoding_peptide.append(sub_rna)
     return pattern_encoding_peptide

