"""

 Created on 11-Apr-21
 @author: Kiril Zelenkovski

 Complementing a Strand of DNA: http://rosalind.info/problems/revc/

"""
from Bio.Seq import Seq

with open('rosalind_revc.txt', 'r') as file:
    sample_dataset = file.read().replace('\n', '')

input_dna = Seq(sample_dataset)
output_rna = input_dna.reverse_complement()
print(output_rna)