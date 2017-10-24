#!/usr/bin/env python3
#Python_06 question 3
#myscript_23.txt


#Using pattern matching, find all the header lines in Python_06.fasta.
#line-by-line isntead of making the file object read it as one string

import re

fastafile = open ("../Python_06.fasta.txt", "r")

for line in fastafile:
        if re.search(r">\S+.+", line):
                print(line)


