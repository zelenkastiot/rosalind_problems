"""

 Created on 12-Feb-21
 @author: Kiril Zelenkovski
 @source: Reproducible Bioinformatics - O'Reilly

 solution3.py: Using a Dictionary to Count all the Characters;

 Counting DNA nucleotides: http://rosalind.info/problems/dna/

"""

with open('rosalind_dna.txt', 'r') as file:
    dna = file.read().replace('\n', '')

def count(dna_dataset: str):
    """ Count bases in DNA """

    counts = {}
    for base in dna_dataset:
        if base not in counts:
            counts[base] = 0
        counts[base] += 1

    return (counts.get('A', 0),
            counts.get('C', 0),
            counts.get('G', 0),
            counts.get('T', 0))

if __name__ == '__main__':
    count_a, count_c, count_g, count_t = count(dna)
    print(f'{count_a} {count_c} {count_g} {count_t}')
