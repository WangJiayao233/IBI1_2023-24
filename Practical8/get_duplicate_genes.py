import os
import re
os.chdir('/Users/wangjiayao/Desktop/Python/Notes/IBI1_2023-24/IBI1_2023-24/Practical8')
gene = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
cnt1 = 0
cnt2 = 0
for line in gene:
    if line.startswith('>'):
        #When the line with "duplication;" is found, create a file called "duplicate_genes.fa" 
        #and write the first gene name into it.

        #cnt1 == 0 means this is the first time to find duplication in the line with ">"
        if re.search('duplication;',line) and cnt1 == 0:
            gene_name = re.search('gene:(\w+)',line)
            fout = open('duplicate_genes.fa','w')
            fout.write(gene_name.group(1))
            fout.write('\n')
            cnt1 = 1
            cnt2 = 1
        #Because the "write" will overwrite the file, we need to use "a" to add the next gene name into the file.
        #use 'a' to avoid overwriting the file.
        elif re.search('duplication;',line) and cnt1 == 1:
             gene_name = re.search('gene:(\w+)',line)
             fout = open('duplicate_genes.fa','a')
             fout.write(gene_name.group(1))
             fout.write('\n')
             cnt2 = 1
        else:
            cnt2 = 0
            continue
    else:
        #cnt2 is used to check if the sequences is just after the line with "duplication" and ">".
        if cnt2 == 1:
            fout = open('duplicate_genes.fa','a')
            fout.write(line)
        else:
            continue   
fout.close()

