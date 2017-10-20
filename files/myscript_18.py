#!/usr/bin/env python3
#Python_05 question 3


fasta_read = open ("../Python_05comb.fasta", "r")
fasta_write = open ("../Python_05comb_RC.fasta", "w")

for dna in fasta_read:
	dna = dna.rstrip()
	
	if dna.startswith('>'):
		fasta_write.write(dna + " reverse complement" + "\n")	

	else:
		dna_reverse= dna.replace('T', 'a').replace('A', 't').replace('G', 'c').replace('C', 'g')
		fasta_write.write(dna_reverse[::-1] + "\n")		

fasta_read.close()
fasta_write.close()


#dna_reverse= dna.replace('T', 'a').replace('A', 't').replace('G', 'c').replace('C', 'g')

                #dna_reverse = dna_reverse.rstrip()

        #fasta_write.write(dna_reverse[::-1])

#print ("../Python_05_rc.fasta")
