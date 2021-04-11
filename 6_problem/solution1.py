"""

 Created on 12-Apr-21
 @author: Kiril Zelenkovski

 Translating RNA into Protein: http://rosalind.info/problems/prot/

"""
from Bio.Seq import Seq

with open('rosalind_prot.txt', 'r') as file:
    sample_dataset = file.read().replace('\n', '')

messenger_rna = Seq(sample_dataset)
protein_seq = messenger_rna.translate(to_stop=True)

print(protein_seq)