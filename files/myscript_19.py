#!/usr/bin/env python3
#Python_05 question 4

linecount = 0
chrcount = 0

fastq = open ("../Python_05.fastq", "r")

for line in fastq:
	line = line.rstrip("\n")
	linecount+= 1
	chrcount += len(line)

print ("linecount:", linecount)
print ("chrcount:", chrcount )
print ("avglinelength:", (chrcount/linecount) )

