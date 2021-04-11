"""

 Created on 11-Apr-21
 @author: Kiril Zelenkovski

 Counting Point Mutations: http://rosalind.info/problems/hamm/

"""
with open('rosalind_hamm.txt', 'r') as file:
    data = file.readlines()

# Пример dataset
# dna      = "GAGCCTACTAACGGGAT"
# mutation = "CATCGTAATGACGGCCT"

# Тест dataset
dna = data[0]
mutation = data[1]

def hamming_distance(str_1, str_2):
    return len([(n1, n2) for n1, n2 in zip(str_1, str_2) if n1 != n2])

print(hamming_distance(dna, mutation))

