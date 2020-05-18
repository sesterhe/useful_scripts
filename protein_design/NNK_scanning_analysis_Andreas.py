#!/usr/bin/env python

from Bio.SeqIO.QualityIO import FastqGeneralIterator
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
import math


WT = 'GGTATCAAAGTCAAATGCCCGAAAGGCGGTGAATGTACGATTAAAGACAGTCAACGTGGCATTATCAAAACCTTTAGCTCTGGTACGGAAGAAGTTCGCAGTCCGTCCCTGGGCAAAGTGACCGTTGGT'

def read_fastq(filename):
    fastq = []
    with open(filename, 'rU') as fastq_file:
        for title, seq, qual in FastqGeneralIterator(fastq_file):
            fastq.append((title, seq.rstrip('>')))
    return fastq


def compare_nucleotide_wt_to_design(wt, design):
    if 2 < len([aa[0].upper() + str(num+1) + aa[1].upper() for num, aa in enumerate(zip(wt, design)) if aa[0] != aa[1]]) < 4:
        return True
    else:
        return False

def compare_aminoacid_wt_to_design(wt, design):
    if len([aa[0].upper() + str(num + 1) + aa[1].upper() for num, aa in enumerate(zip(wt, design)) if aa[0] != aa[1]]) < 2:
        return True
    else:
        return False


def convert_nt_to_aa(nt):
    gene = Seq(nt, generic_dna)
    return str(gene.translate(table="Bacterial"))





if __name__ == "__main__":
    fastq = read_fastq("top2.fastq")
    counter = 0
    aa_mutations = []
    for tuple in fastq:
        if not "N" in tuple[1] and compare_nucleotide_wt_to_design(WT, tuple[1]):
            if compare_aminoacid_wt_to_design(convert_nt_to_aa(WT), convert_nt_to_aa(tuple[1])):
                # print tuple
                counter+=1
                if len([aa[0].upper() + str(num+1) + aa[1].upper() for num, aa in enumerate(zip(convert_nt_to_aa(WT), convert_nt_to_aa(tuple[1]))) if aa[0] != aa[1]]) > 0:
                    aa_mutations.append([(num+1, aa[1].upper()) for num, aa in enumerate(zip(convert_nt_to_aa(WT), convert_nt_to_aa(tuple[1]))) if aa[0] != aa[1]][0])
                else:
                    aa_mutations.append([(int(math.floor(num/3)+1), convert_nt_to_aa(tuple[1])[int(math.floor(num/3))]) for num, aa in enumerate(zip(WT,tuple[1])) if aa[0] != aa[1]][0])

    # print aa_mutations
    print counter
    pos_9 = {}
    pos_11 = {}
    pos_13 = {}
    pos_16 = {}
    pos_27 = {}
    pos_30 = {}
    pos_34 = {}
    pos_36 = {}
    pos_39 = {}
    pos_41 = {}

    for mutation in aa_mutations:
        if mutation[0] == 9:
            if pos_9.has_key(mutation[1]):
                pos_9.update({mutation[1]: pos_9.get(mutation[1])+1})
            else:
                pos_9.update({mutation[1]: 1})
        if mutation[0] == 11:
            if pos_11.has_key(mutation[1]):
                pos_11.update({mutation[1]: pos_11.get(mutation[1])+1})
            else:
                pos_11.update({mutation[1]: 1})
        if mutation[0] == 13:
            if pos_13.has_key(mutation[1]):
                pos_13.update({mutation[1]: pos_13.get(mutation[1])+1})
            else:
                pos_13.update({mutation[1]: 1})
        if mutation[0] == 16:
            if pos_16.has_key(mutation[1]):
                pos_16.update({mutation[1]: pos_16.get(mutation[1])+1})
            else:
                pos_16.update({mutation[1]: 1})
        if mutation[0] == 27:
            if pos_27.has_key(mutation[1]):
                pos_27.update({mutation[1]: pos_27.get(mutation[1])+1})
            else:
                pos_27.update({mutation[1]: 1})
        if mutation[0] == 30:
            if pos_30.has_key(mutation[1]):
                pos_30.update({mutation[1]: pos_30.get(mutation[1])+1})
            else:
                pos_30.update({mutation[1]: 1})
        if mutation[0] == 34:
            if pos_34.has_key(mutation[1]):
                pos_34.update({mutation[1]: pos_34.get(mutation[1])+1})
            else:
                pos_34.update({mutation[1]: 1})
        if mutation[0] == 36:
            if pos_36.has_key(mutation[1]):
                pos_36.update({mutation[1]: pos_36.get(mutation[1])+1})
            else:
                pos_36.update({mutation[1]: 1})
        if mutation[0] == 39:
            if pos_39.has_key(mutation[1]):
                pos_39.update({mutation[1]: pos_39.get(mutation[1])+1})
            else:
                pos_39.update({mutation[1]: 1})
        if mutation[0] == 41:
            if pos_41.has_key(mutation[1]):
                pos_41.update({mutation[1]: pos_41.get(mutation[1])+1})
            else:
                pos_41.update({mutation[1]: 1})


    print "pos 9: {}".format(pos_9)
    print "pos 11: {}".format(pos_11)
    print "pos 13: {}".format(pos_13)
    print "pos 16: {}".format(pos_16)
    print "pos 27: {}".format(pos_27)
    print "pos 30: {}".format(pos_30)
    print "pos 34: {}".format(pos_34)
    print "pos 36: {}".format(pos_36)
    print "pos 39: {}".format(pos_39)
    print "pos 41: {}".format(pos_41)
