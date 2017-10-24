#!/usr/bin/env python3

import re

file = open ("../blast_rand5-200_v_qfo_BLOSUM62.txt", "r")

BLOS62_200 = {}

for line in file:
	line=line.rstrip()
		
	notes = line.startswith('#')	
	if not notes:
		split=line.split('\t')

BLOS62_200['BLOS62_200']=split

#print(BLOS62_200)

file.close()					

file2 = open ("../blast_rand5-800_v_qfo_BLOSUM62.txt", "r")

BLOS62_800 = {}

for line2 in file2:
        line2=line2.rstrip()

        notes2 = line2.startswith('#') 
        if not notes2:
                split2=line2.split('\t')

BLOS62_800['BLOS62_800']=split2

#print(BLOS62_800)

BLOS62 = {}

BLOS62['200'] = BLOS62_200
BLOS62['800'] = BLOS62_800

blah1=(BLOS62['200']['BLOS62_200'][2:4])
print(blah1)

blah1.append(BLOS62['200']['BLOS62_200'][10])

print(blah1)





***this only printed BLOSUM62 200 line; will need to specify the 800 line and other files... too complicated



JARRYD'S SCRIPT IS MUCH BETTER


#!/usr/bin/env python3
from glob import glob

direc = glob('./*.txt')
BLAST_dict = {}

for file in direc:
    files = open(file, "r")
    for line in files:
        line_strip = line.strip()
        if line_strip.startswith('#'):
            continue
        else:
            BLAST_dict[file] = line_strip.split('\t')

for key,value in BLAST_dict.items():
    print(key," - ", "\n Percent ID:", value[2], "\n Alignment Length:", value[3], "\n E-Value:", value[10], "\n Query Length:$




