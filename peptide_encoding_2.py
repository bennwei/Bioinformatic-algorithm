


def DNA_to_RNA(DNA_file):
    """Return dna string as rna string.
    >>>DNA_to_RNA('CCGGAAGAGCTTACTTAG')
    'CCGGAAGAGCUUACUUAG' 
    """
    DNA_seq = open(DNA_file)
    DNA = DNA_seq.readline().strip()
    RNA = DNA.replace('T', 'U')
    return RNA

def make_codon_dictionary(filename):
    codon_table = {}
    with open(filename) as f:
         for line in f:
             if " \n" in line:
                 triplet = line.strip()
                 codon_table[triplet] = "stop"
             else:
                 (triplet, aa) = line.strip().split(" ")
                 codon_table[triplet] = aa
                 return codon_table

def RNA_to_Protein(RNA, codon_table):
     """
     Protein Translation Problem: Translate an RNA string into an amino acid string.
     Input: An RNA string Pattern and the array GeneticCode.
     Output: The translation of Pattern into an amino acid string Peptide.
     >>>RNA_to_Protein('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA')
     MAMAPRTEINSTRING
     """
     protein = ' '
     for i in xrange(0, len(RNA)-2, 3):
         codon = RNA[i:i+3]
         if codon_table[codon] != "stop":
             protein += codon_table[codon]
         else:
             break
     return protein
    
def pattern_encoding_in_rna(RNA, peptide, codon_table):
     pattern_encoding_peptide = [ ]
     for i in range(len(RNA) - 3*len(peptide) +1):
         sub_rna = RNA[i : i+3*len(peptide)]
         sub_peptide = RNA_to_Protein(RNA, codon_table)
         sub_peptide_reverse = 
         if sub_peptide == peptide:
             pattern_encoding_peptide.append(sub_rna)
     return pattern_encoding_peptide

