import re 
#set the sequence of a part of DNA
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
#find the number of times the pattern GTGTGT or GTCTGT occurs in the sequence
l=re.findall('(?=(GT(G|C)TGT))',seq)
#findall return a list
print(len(l))


