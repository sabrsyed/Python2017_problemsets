#!/usr/bin/env python3

import re
import Bio.Seq
from Bio import SeqIO

sprotfasta = open ("../uniprot_sprot.fasta", "r")
count = 0

for record in sprotfasta:
        count +=1

print(count)
