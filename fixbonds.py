# -*-
# @project: pymol-scripts
# @file:    fix_bonds.py
#
# @author: jaume.bonet
# @email:  jaume.bonet@gmail.com
# @url:    jaumebonet.cat
#
# @date:   2017-02-23 15:56:59
#
# @last modified by:   jaume.bonet
# @last modified time: 2017-02-26 10:37:16
#
# -*-

from pymol import cmd, stored

def state2frame(selection, start=1):
    for i, x in enumerate(list(range(int(start), int(start) + cmd.count_states(selection) + 1))):
        cmd.frame(x)
        cmd.set('state', str(i + 1), selection)
        print ("Frame => %s; and State => %s" % ( str(x), str(i + 1)))

def all_distances(selection, min_seq_dist=6, max_seq_dist=40, min_seq = 0, max_seq = 0):

    stored.ca = []
    cmd.iterate( selection + ' and n. ca', 'stored.ca.append((resi, resn))')

    if max_seq_dist == 0: max_seq_dist = len(stored.ca)
    if max_seq == 0: max_seq = len(stored.ca)

    for cat1, at1 in enumerate(stored.ca):
        if int(cat1) < int(min_seq): continue
        print (cat1)
        if int(cat1) >= int(max_seq): break
        for cat2, at2 in enumerate(stored.ca):
            if cat2 < cat1: continue
            if int(cat2) >= int(max_seq): break
            if cat2 > cat1 + int(min_seq_dist) and cat2 < cat1 + int(max_seq_dist):
                sele1 = selection + " and r. " + str(at1[1]) + " and i. " + str(at1[0]) + " and n. ca"
                sele2 = selection + " and r. " + str(at2[1]) + " and i. " + str(at2[0]) + " and n. ca"
                print ("distance ", "dist_" + str(cat1) + "_" + str(cat2), ",", sele1, ",", sele2)
                cmd.distance("dist_" + str(cat1) + "_" + str(cat2), sele1, sele2)
    cmd.group(selection + "_dists", "dist_*")

def fix_bonds(selection):

    stored.residues = []
    cmd.iterate( selection + ' and n. ca', 'stored.residues.append((resi,resn))')
    last_residue = stored.residues[-1][0]
    print (last_residue)
    for r1 in range(len(stored.residues)):
        residue1 = selection + " and r. " + stored.residues[r1][1] + " and i. " + stored.residues[r1][0]
        sele1 = residue1 + " and n. ca+c+c+o+n"
        sele2 = residue1 + " and !n. ca+c+c+o+n+cb"
        print ("unbond ", sele1, ",", sele2)
        cmd.unbond(sele1, sele2)
        for r2 in range(r1 + 1, len(stored.residues)):
            residue2 = selection + " and r. " + stored.residues[r2][1] + " and i. " + stored.residues[r2][0]
            if int(stored.residues[r1][0]) != int(stored.residues[r2][0]):
                sele1 = residue1
                sele2 = residue2
                print ("unbond ", sele1, ",", sele2)
                cmd.unbond(sele1, sele2)
            if int(stored.residues[r2][0]) == (int(stored.residues[r1][0]) + 1):
                sele1 = residue1 + " and n. c"
                sele2 = residue2 + " and n. n"
                print ("bond ", sele1, ",", sele2)
                cmd.bond(sele1, sele2)

        # FIX RESIDUE SIDE CHAIN
        if stored.residues[r1][1] == "PRO":
            sele1 = residue1 + " and n. n"
            sele2 = residue1 + " and n. cd"
            print ("bond ", sele1, ",", sele2)
            cmd.bond(sele1, sele2)
        elif stored.residues[r1][1] == "THR":
            sele1 = residue1 + " and !n. ca+og1+cg2+cb"
            sele2 = residue1 + " and n. cb"
            print ("unbond ", sele1, ",", sele2)
            cmd.unbond(sele1, sele2)
        elif stored.residues[r1][1] == "ILE" or stored.residues[r1][1] == "VAL":
            for resitype in ["ILE", "VAL"]:
                sele1 = residue1 + " and !n. ca+cg1+cg2+cb"
                sele2 = residue1 + " and n. cb"
                print ("unbond ", sele1, ",", sele2)
                cmd.unbond(sele1, sele2)
        elif stored.residues[r1][1] == "SER":
            sele1 = residue1 + " and !n. ca+og+cb"
            sele2 = residue1 + " and n. cb"
            print ("unbond ", sele1, ",", sele2)
            cmd.unbond(sele1, sele2)
        elif stored.residues[r1][1] == "CYS":
            sele1 = residue1 + " and !n. ca+sg+cb"
            sele2 = residue1 + " and n. cb"
            print ("unbond ", sele1, ",", sele2)
            cmd.unbond(sele1, sele2)
        else:
            sele1 = residue1 + " and !n. ca+cg+cb"
            sele2 = residue1 + " and n. cb"
            print ("unbond ", sele1, ",", sele2)
            cmd.unbond(sele1, sele2)

        # FIX CENTROID LEVEL
        sele1 = residue1 + " and n. cen"
        sele2 = residue1 + " and n. cb"
        print ("bond ", sele1, ",", sele2)
        cmd.bond(sele1, sele2)

        # FIX C-TERMINAL
        if stored.residues[r1][0] == last_residue:
            sele1 = residue1 + " and n. c"
            sele2 = residue1 + " and n. oxt"
            print ("bond ", sele1, ",", sele2)
            cmd.bond(sele1, sele2)

    stored.cys = []
    cmd.iterate( selection + ' and r. CYS and n. cb', 'stored.cys.append((resi,resn))')
    if len(stored.cys) >= 2:
        for r1 in range(len(stored.cys)):
            for r2 in range(r1 + 1, len(stored.cys)):
                if stored.cys[r1][0] != stored.cys[r2][0]:
                    sele1 = selection + " and i. " + stored.cys[r1][0] + " and n. cb"
                    sele2 = selection + " and i. " + stored.cys[r2][0] + " and n. cb"
                    dist  = cmd.distance("tmpdist", sele1, sele2)
                    if dist < 4.0:
                        print (dist, sele1, ",", sele2)
                        sele1 = selection + " and i. " + stored.cys[r1][0] + " and n. sg"
                        sele2 = selection + " and i. " + stored.cys[r2][0] + " and n. sg"
                        print ("bond ", sele1, ",", sele2)
                        cmd.bond(sele1, sele2)
    cmd.delete("tmpdist")


cmd.extend('fix_bonds', fix_bonds)
cmd.extend('all_distances', all_distances)
cmd.extend('state2frame', state2frame)
