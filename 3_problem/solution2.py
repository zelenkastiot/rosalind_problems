"""

 Created on 11-Apr-21
 @author: Kiril Zelenkovski

 Complementing a Strand of DNA: http://rosalind.info/problems/revc/

"""
with open('rosalind_revc.txt', 'r') as file:
    dna = file.read().replace('\n', '')

st = dna.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
print(st)