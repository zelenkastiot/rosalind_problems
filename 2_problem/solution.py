"""

 Created on 11-Apr-21
 @author: Kiril Zelenkovski

 Transcribing DNA into RNA: http://rosalind.info/problems/rna/

"""

from Bio.Seq import Seq

with open('rosalind_rna.txt', 'r') as file:
    sample_dataset = file.read().replace('\n', '')

input_dna = Seq(sample_dataset)
output_rna = input_dna.transcribe()
print(output_rna)