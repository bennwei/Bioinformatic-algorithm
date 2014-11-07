class DNA(object):
    def __init__(self, DNA, peptides, codon_table):
        self.DNA = DNA
        self.peptides = peptides
        self.codon_table = codon_table
        
    def transcribe_DNA(self):
        """Return dna string as rna string.
    >>>DNA_to_RNA('CCGGAAGAGCTTACTTAG')
    'CCGGAAGAGCUUACUUAG' 
    """
        RNA = self.replace('T', 'U')
        return RNA
        
    