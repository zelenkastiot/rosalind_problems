"""

 Created on 11-Feb-21
 @author: Kiril Zelenkovski

 solution.py: Basic count;

 Counting DNA nucleotides: http://rosalind.info/problems/dna/

"""

with open('rosalind_dna.txt', 'r') as file:
    dna = file.read().replace('\n', '')

count_a = 0
count_g = 0
count_c = 0
count_t = 0

for base in dna:
    if base == 'A':
        count_a += 1
    elif base == 'G':
        count_g += 1
    elif base == 'C':
        count_c += 1
    else:
        count_t += 1

print(f'{count_a} {count_g} {count_c} {count_t}')

