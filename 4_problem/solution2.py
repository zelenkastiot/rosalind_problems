"""

 Created on 11-Apr-21
 @author: Kiril Zelenkovski

 solution2.py: Reading text file, computing GC value

 Computing GC Content: http://rosalind.info/problems/gc/

"""

f = open('rosalind_gc.txt', 'r')


max_gc_name, max_gc_content = '', 0

buf = f.readline().rstrip()
while buf:
    seq_name, seq = buf[1:], ''
    buf = f.readline().rstrip()
    while not buf.startswith('>') and buf:
        seq = seq + buf
        buf = f.readline().rstrip()
    seq_gc_content = (seq.count('C') + seq.count('G'))/float(len(seq))
    if seq_gc_content > max_gc_content:
        max_gc_name, max_gc_content = seq_name, seq_gc_content

print(f"{max_gc_name}\n{max_gc_content*100:.6f}")

f.close()