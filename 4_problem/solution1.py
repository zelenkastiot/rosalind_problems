"""

 Created on 11-Apr-21
 @author: Kiril Zelenkovski

 solution1.py: Reading fasta file, computing GC value

 Computing GC Content: http://rosalind.info/problems/gc/

"""
from Bio import SeqIO

dict_records = {}
for seq_record in SeqIO.parse("rosalind_gc.fasta", "fasta"):
    seq_temp = seq_record.seq
    dict_records[seq_record.id] = 100 * float(seq_temp.count("G") + seq_temp.count("C")) / len(seq_temp)

print("Речник од записи: ")
for item in dict_records:
    print(f'{item}: {dict_records[item]}')

max_value = max(dict_records.values())  # max calue
max_keys = [k for k, v in dict_records.items() if v == max_value]  # key for max value

print("\nНајголем запис: ")
print(max_keys[0])
print(f'{max_value:.6f}')
