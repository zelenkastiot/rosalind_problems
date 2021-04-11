"""

 Created on 11-Apr-21
 @author: Kiril Zelenkovski

 Finding a Motif in DNA: http://rosalind.info/problems/subs/

"""

f = open('rosalind_subs.txt').read().split('\n')

s1, s2 = f[0], f[1]

for i in range(len(s1)):
    if s1[i:].startswith(s2):
        print(i+1, end =" ")