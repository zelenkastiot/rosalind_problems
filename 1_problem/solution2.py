"""

 Created on 11-Feb-21
 @author: Kiril Zelenkovski
 @source: Reproducible Bioinformatics - O'Reilly

 solution2.py: Count using the string count function;

 Counting DNA nucleotides: http://rosalind.info/problems/dna/

"""

with open('rosalind_dna.txt', 'r') as file:
    dna = file.read().replace('\n', '')


def count(dna_data: str):
    return dna_data.count('A'), \
           dna_data.count('C'), \
           dna_data.count('G'), \
           dna_data.count('T')

if __name__ == '__main__':
    count_a, count_c, count_g, count_t = count(dna)
    print(f'{count_a} {count_c} {count_g} {count_t}')
