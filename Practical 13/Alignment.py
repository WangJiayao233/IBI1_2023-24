import os
os.chdir('/Users/wangjiayao/Desktop/Python/Notes/IBI1_2023-24/IBI1_2023-24/Practical 13')

def read_seq(file):
    seq = ""
    for line in file:
        if line.startswith('>'):
            continue
        else:
            seq += line.rstrip()
    return seq

def distance(seq1, seq2):
    dis = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            dis += 1
    return dis

file_seq_human = open("SLC6A4_HUMAN.fa", "r")
file_seq_mouse = open("SLC6A4_MOUSE.fa", "r")
file_seq_rat = open("SLC6A4_RAT.fa", "r")

#  read the sequence of human, mouse and rat respectively
seq_human = read_seq(file_seq_human)
seq_mouse = read_seq(file_seq_mouse)
seq_rat = read_seq(file_seq_rat)

# for the relationship between human and mouse
dis_human_mouse = distance(seq_human, seq_mouse)
print(dis_human_mouse)
same_amino = (len(seq_human)-dis_human_mouse)/len(seq_human)
same_amino = round(same_amino, 4)
print(str(same_amino*100) + '%')


# for the relationship between human and rat
dis_human_rat = distance(seq_human, seq_rat)
print(dis_human_rat)
same_amino = (len(seq_human)-dis_human_rat)/len(seq_human)
same_amino = round(same_amino, 4)
print(str(same_amino*100) + '%')

# for the relationship between mouse and rat
dis_mouse_rat = distance(seq_mouse, seq_rat)
print(dis_mouse_rat)
same_amino = (len(seq_mouse)-dis_mouse_rat)/len(seq_mouse)
same_amino = round(same_amino, 4)
print(str(same_amino*100) + '%')

