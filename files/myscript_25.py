
#!/usr/bin/env python3
#Python_06 question 4   
#myscript_24.txt


#extract the sequence name and description using sub patterns (groups)

import re

fastafile = open ("../Python_06.fasta.txt", "r")


for line in fastafile:
	line=line.rstrip()
	found= re.search(r">(\S+)\s(.+)", line)
	if found:
		 print("id:", found.group(1), "desc:", found.group(2) )

	else: 
		print(line)



