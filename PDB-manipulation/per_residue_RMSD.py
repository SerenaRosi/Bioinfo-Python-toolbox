#!/usr/bin/env python

from Bio.PDB import *
import sys
import pybel
import math
import os

def squared_distance(coordsA, coordsB):
    """Find the squared distance between two 3-tuples"""
    sqrdist = sum( (a-b)**2 for a, b in zip(coordsA, coordsB) )
    return sqrdist
    
def rmsd(allcoordsA, allcoordsB):
    """Find the RMSD between two lists of 3-tuples"""
    deviation = sum(squared_distance(atomA, atomB) for 
                    (atomA, atomB) in zip(allcoordsA, allcoordsB))
    return math.sqrt(deviation / float(len(allcoordsA)))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("ERROR \nCorrect Usage: res_flex.py path/to/dir <PDB_file>")	
        sys.exit(1)

parser = PDBParser()

residue_list = []

s2 = next(pybel.readfile("pdb", sys.argv[2]))
structure2 = parser.get_structure('s2', sys.argv[2])           
residue2 = structure2[0]['A'][220]
a = [tuple(atom2.get_coord()) for atom2 in residue2]
#print(a)

for filename in os.listdir(sys.argv[1]):
    if filename.endswith((".pdb")):
        s1 = next(pybel.readfile("pdb", filename))
        structure = parser.get_structure('s1', filename)           
        residue1 = structure[0]['A'][220]
        b = [tuple(atom1.get_coord()) for atom1 in residue1]
        #print(b)
        value = rmsd(a, b)
        print(value)
                     
