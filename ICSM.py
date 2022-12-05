

from Bio import SeqIO
    
def shortest_seq(seq):
    minmum_len = 10000
    shortest_seq = ''
    for i in seq.keys():
        if len(seq[i]) < minmum_len:
            minmum_len = len(seq[i])
            shortest_seq = seq[i]
    return shortest_seq

def shared_motif(seq):
    s_seq = shortest_seq(seq)
    ICSM = set()
    for i in range(len(s_seq)):
        for j in range(i+1,len(s_seq)+1):
            ICSM.add(s_seq[i:j])
    for s in seq.values():
        update_motif = list(ICSM)
        for m in update_motif:
            if m not in s:
                ICSM.remove(m)
    n = 0
    longest_motif = ''
    for i in ICSM:
        if len(i) > n:
            longest_motif = i
            n = len(i)
    return longest_motif

if __name__ == "__main__":
    seq_name, seq_string = [], []
    with open (r"C:\Users\robin\Downloads\rosalind_lcsm.txt",'r') as fa:
        for seq_record  in SeqIO.parse(fa,'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))
    seq = {seq_name[i]:seq_string[i] for i in range(len(seq_name))}
    print(shared_motif(seq))