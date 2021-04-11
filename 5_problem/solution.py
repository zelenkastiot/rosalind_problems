"""

 Created on 11-Apr-21
 @author: Kiril Zelenkovski

 Finding a Motif in DNA: http://rosalind.info/problems/subs/

"""
file = open('rosalind_subs.txt', 'r')

Lines = file.readlines()

dna_string = Lines[0].strip()
sub_string = Lines[1].strip()

found = []

k = 0
while k < len(dna_string)-3:
    current_codon = dna_string[k:k+(len(sub_string))]
    if current_codon == sub_string:
        found.append(k+1)
    k+=1

for i in range(len(found)):
    print(found[i], end=" ")
