#!/usr/bin/env python3
#uploaded to github repository: https://github.com/hannahoday/bch5884.git
#bch5884 RMSD code
#author Hannah O'Day

import sys
import math


#function readfile
#reads provided args
def readfile(argnum):
    pdbfilename=sys.argv[argnum]
    f=open(pdbfilename)
    lines=f.readlines()
    f.close()
    records=[]
    massdict={"H":1.01, "C":12.01,"N":14.01,"O":16.0, "P":30.97, "S":32.07,"MG":24.30}
    countlines = len(lines)
    #detects if "END" line is present, deletes line
    if countlines==1338:
        lines=lines[:-1]
    #parses into list of atoms
    for line in lines:
        atom=line[0:6].strip()
        integer=line[7:11].strip()
        name=line[13:16].strip()
        altloc=line[16:17].strip()
        resname=line[17:20].strip()
        chainID=line[21:22]
        resSeq=line[22:26].strip()
        icode=line[26:27]
        x=float(line[30:38])
        y=float(line[39:46])
        z=float(line[47:54])
        occ=line[55:60].strip()
        temp=line[61:66].strip()
        element=line[76:78].strip()
        mass=massdict[element]
        records.append([atom,integer,name,altloc,resname,chainID,resSeq,icode,x,y,z,occ,temp,element,mass])    
    return records

#function rmsd
#calculates rmsd from lists
def rmsd(atomlist1,atomlist2):
    sum=0
    i=0
    for x in atomlist1:
        sum=sum+(x[8]-atomlist2[i][8])**2+(x[9]-atomlist2[i][9])**2+(x[10]-atomlist2[i][10])**2
        i=i+1
    root=math.sqrt((1/i)*sum)
    print(root)

  
l1=readfile(1)
l2=readfile(2)
rmsd(l1,l2)




