#!/usr/bin/env python3
import sys

def get_seqs(fileseq):
    dseq = dict()
    f = open(fileseq)
    for line in f:
        if line[0] == '>':
            k = line.split('|')[1]
            dseq[k] = ''
            continue
        dseq[k] += line.rstrip()
    return dseq


if __name__ == '__main__':
    fields = sys.argv[1]
    fileseq = sys.argv[2]
    dseq = get_seqs(fileseq)
    ids = open(fields).read().rstrip().split('\n')
    for i in ids:
        if dseq.get(i, 0) != 0:
            print(">" + i + '\n' + dseq[i])