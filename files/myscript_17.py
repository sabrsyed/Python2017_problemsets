#!/usr/bin/env python3
#Python_05 question 3


fasta_read = open ("../Python_05.fasta", "r")
fasta_write = open ("../Python_05comb.fasta", "w")

combined = ""

for dna in fasta_read:
	dna = dna.rstrip()
	
	if dna.startswith('>'):
		if combined:
			fasta_write.write(combined + "\n")
		combined = ""
		fasta_write.write(dna + "\n")
	
	else:
		combined += dna

fasta_write.write(combined + "\n")





	#dna = dna.rstrip()
		
#dna_reverse= dna.replace('T', 'a').replace('A', 't').replace('G', 'c').replace('C', 'g')
		
		#dna_reverse = dna_reverse.rstrip()
		
	#fasta_write.write(dna_reverse[::-1])

#print ("../Python_05_rc.fasta")

fasta_read.close()
fasta_write.close()


