#!/usr/bin/env python3

import re

sprotfasta = open ("../uniprot_sprot.fasta", "r")

recordID = []

for record in sprotfasta:
	found = re.search(r"(OS=.+)(\sGN)", record)
	if found:
		recordID.append(found.group(1))

print(recordID)
