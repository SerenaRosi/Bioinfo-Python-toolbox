#!/usr/bin/env python

from Bio.PDB import *
import sys
import pybel
import math
import os

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR \nCorrect Usage: angle.py <file>.pdb")	
        sys.exit(1)

parser = PDBParser()

for filename in os.listdir(sys.argv[1]):
    if filename.endswith((".pdb")):
        s = next(pybel.readfile("pdb", filename))
        structure = parser.get_structure('s', filename)

        atom1 = structure[0]['A'][174]['CA']
        atom2 = structure[0]['A'][308]['CA']
        atom3 = structure[0]['A'][324]['CA']

        v1 = atom1.get_vector()
        v2 = atom2.get_vector()
        v3 = atom3.get_vector()

        angle = calc_angle(v1, v2, v3)
        print(math.degrees(angle)) 

