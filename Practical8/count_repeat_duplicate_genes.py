import re
import os
os.chdir('/Users/wangjiayao/Desktop/Python/Notes/IBI1_2023-24/IBI1_2023-24/Practical8')
gene = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')

rep_seq = input('Please input the repetitive sequence here: ')
open(rep_seq+'_duplicate_genes.fa','w')
open('temp.fa','w')

#Line 11 to 45 is adapted from my script--the get_duplicate_genes.py
cnt1 = 0
cnt2 = 0
for line in gene:
    if line.startswith('>'):
        #When the line with "duplication;" is found, create a file called "duplicate_genes.fa" 
        #and write the first gene name into it.
        #cnt1 == 0 means this is the first time to find duplication in the line with ">"
        if re.search('duplication;',line) and cnt1 == 0:
            gene_name = re.search('gene:(\w+)',line)
            fout = open('temp.fa','w')
            fout.write(gene_name.group(1))
            fout.write('\n')
            cnt1 = 1
            cnt2 = 1
        #Because the "write" will overwrite the file, we need to use "a" to add the next gene name into the file.
        #use 'a' to avoid overwriting the file.
        elif re.search('duplication;',line) and cnt1 == 1:
             gene_name = re.search('gene:(\w+)',line)
             fout = open('temp.fa','a')
             fout.write('\n')
             fout.write(gene_name.group(1))
             fout.write('\n')
             cnt2 = 1
        else:
            cnt2 = 0
            continue
    else:
        #cnt2 is used to check if the sequences is just after the line with "duplication" and ">".
        if cnt2 == 1:
            fout = open('temp.fa','a')
            line = line.rstrip()
            fout.write(line)
        else:
            continue 
fout.close()  

#use a temporary file to restore the sequences of duplication.
dupilicate_seq = open('temp.fa','r')
list_seq = dupilicate_seq.readlines()
line_cnt = 0 #count the line number
for line in list_seq:
    if len(re.findall(rep_seq, line)) > 0:
        fout2 = open(rep_seq+'_duplicate_genes.fa','a')
        list_seq[line_cnt-1] = list_seq[line_cnt-1].rstrip()
        if rep_seq == 'GTGTGT':
            fout2.write(list_seq[line_cnt-1]+' '+str(len(re.findall('(?=(GTGTGT))',line)))+'\n')
        elif rep_seq == 'GTCTGT':
            fout2.write(list_seq[line_cnt-1]+' '+str(len(re.findall('(?=(GTCTGT))',line)))+'\n')
        fout2.write(line)
        line_cnt += 1
    elif len(re.findall(rep_seq,line)) == 0:
        line_cnt += 1
        continue
    else: #avoid some bugs maybe
        line_cnt += 1 
        continue
dupilicate_seq.close()
fout2.close()

os.remove('temp.fa')