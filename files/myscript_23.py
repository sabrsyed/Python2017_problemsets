#!/usr/bin/env python3
#Python_06 question 3
#myscript_23.txt


#Using pattern matching, find all the header lines in Python_06.fasta.

import re

fasta = open ("../Python_06.fasta.txt", "r")

#fastastr= fasta.read()

#header=re.findall(r"^>\S+.+", fastastr)
#print(header)


#for fasta in re.findall(r"(>\S+.+\n)", fastastr):
#	print(descriptor)


for line in fasta:
	if re.search(">\S+.+\n", fasta):
		print(line)
