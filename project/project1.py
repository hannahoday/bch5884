
#!/usr/bin/env python3

#bch5884 project1 code
#author Hannah O'Day
#uploaded to github repository: https://github.com/hannahoday/bch5884.git

import sys

#reading pdb file from argv
#asking user for geometric (G) or center of mass (M)
pdbfilename=sys.argv[1]
choice=input("This program will create a new file of name: 'centered2FA9noend.pdb'\nTo select method of centering, Type 'G' for geometric center or 'M' for center by mass:")
f=open(pdbfilename)
lines=f.readlines()
f.close()

#var records=list of lists for parsed pdb file
records=[]
massdict={"H":1.01, "C":12.01,"N":14.01,"O":16.0, "P":30.97, "S":32.07,"MG":24.30}
for line in lines:
    atom=line[0:6].strip()
    integer=line[7:11].strip()
    name=line[13:16].strip()
    altloc=line[16].strip()
    resname=line[17:20].strip()
    chainID=line[21]
    resSeq=line[22:26].strip()
    icode=line[26]
    x=float(line[30:38])
    y=float(line[39:46])
    z=float(line[47:54])
    occ=line[55:60].strip()
    temp=line[61:66].strip()
    element=line[76:78].strip()
    mass=massdict[element]
    records.append([atom,integer,name,altloc,resname,chainID,resSeq,icode,x,y,z,occ,temp,element,mass])

#setting var values to 0 for loop operations
sumx=0
sumy=0
sumz=0
length=len(records)
mass=0
avgx=0
avgy=0
avgz=0

#center mass calculation
if choice=="M":
    for record in records:
        sumx=sumx+(record[8]*record[14])
        sumy=sumy+(record[9]*record[14])
        sumz=sumz+(record[10]*record[14])
        mass=mass+record[14]
    avgx=sumx/mass
    avgy=sumy/mass
    avgz=sumz/mass

#geometric calculation
elif choice=="G":
    for record in records:
        sumx=sumx+record[8]
        sumy=sumy+record[9]
        sumz=sumz+record[10]
    avgx=sumx/length
    avgy=sumy/length
    avgz=sumz/length

#changing coordinates based on center
#setting new values to records
for record in records:
        record[8]=record[8]-avgx
        record[9]=record[9]-avgy
        record[10]=record[10]-avgz

#creating new file
#writing formatted string
newf=open("centered2FA9noend.pdb","w")
for record in records:
    newf.write("%-6s%5s  %-3s%1s%-3s %1s%4s%1s   %8.3f%8.3f%8.3f %5s%6s%12s\n" % (record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13]))
newf.close


