"""

 Created on 11-Apr-21
 @author: Kiril Zelenkovski

 Transcribing DNA into RNA: http://rosalind.info/problems/rna/

"""
with open('rosalind_rna.txt', 'r') as file:
    dna = file.read().replace('\n', '')

rna = dna.replace("T", "U")
print(rna)