#! /usr/bin/python


import os,sys

def read_pdbs(pdbs):
        seqlist = []
        for n in range(1,len(pdbs)):
                seq = ''
                #print n.strip()
                pdbtext = open(pdbs[n],'r')

                for l in pdbtext.readlines():
                        #print l
                        lines = l.split()
                        if len(lines) > 4 and lines[0] == 'ATOM':
                                if l[13:15] == 'CA':
                                        #print aa_translator(l[17:20]),'\t', l[17:20]
                                        seq += aa_translator(l[17:20])
                seqlist.append((pdbs[n],seq))

        return seqlist

def count_muts(seqlist):
        print 'RES','\t',seqlist[0][0],'\t',seqlist[1][0]
        muts = 0
	string_mut = ''
        for k in range(len(seqlist[0][1])):
                #print seqlist[0][1][k]
                if seqlist[0][1][k] != seqlist[1][1][k]:
                        print k+1,'\t',seqlist[0][1][k],'\t',seqlist[1][1][k]
                        muts += 1
			string_mut += str(k+1)+"+" 
	print 'Number of mutations:','\t', muts
	print 'pymol string:\t', string_mut   
                #if n[1][k]


def aa_translator(aa):
        if aa == 'ALA':
                return 'A'
        if aa == 'ARG':
                return 'R'
        if aa == 'ASN':
                return 'N'
        if aa == 'ASP':
                return 'D'
        if aa == 'CYS':
                return 'C'
        if aa == 'GLU':
                return 'E'
        if aa == 'GLN':
                return 'Q'
        if aa == 'GLY':
                return 'G'
        if aa == 'HIS':
                return 'H'
        if aa == 'ILE':
                return 'I'
        if aa == 'LEU':
                return 'L'
        if aa == 'LYS':
                return 'K'
        if aa == 'MET':
                return 'M'
        if aa == 'PHE':
                return 'F'
        if aa == 'PRO':
                return 'P'
        if aa == 'SER':                                                                         return 'S'
        if aa == 'THR':
                return 'T'
        if aa == 'TRP':
                return 'W'
        if aa == 'TYR':
                return 'Y'
        if aa == 'VAL':
                return 'V'


if len(sys.argv) != 3:
        print "Usage: protein_1 protein_2"
        sys.exit()


count_muts(read_pdbs(sys.argv))
