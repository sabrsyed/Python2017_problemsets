#!/usr/bin/env python3
#Python_05 question 3


fasta_read = open ("../Python_05.fasta", "r")
fasta_write = open ("../Python_05_rc.fasta", "w")

for dna in fasta_read:
	
	dna = dna.rstrip()
	dna_reverse= dna.replace('T', 'a').replace('A', 't').replace('G', 'c').replace('C', 'g') 
	fasta_write.write(dna_reverse[::-1])

fasta_read.close()
fasta_write.close()

#fasta revese complement line-by-line (not CORRECT)


