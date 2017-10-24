#!/usr/bin/env python3
#Python_06 question 1

import re

poem_read = open ("../Python_06_nobody.txt", "r")

poem= poem_read.read()
#print(poem)


####Find the first instance of the Nobody

#Nobody=re.search(r"Nobody", poem)
#print(Nobody)
#print("position:", Nobody.pos)

All_Nobody=re.findall(r"Nobody", poem)
print("Nobody count:", All_Nobody.count('Nobody'))

count=0

for match in re.finditer(r"Nobody", poem):
	
	start	= match.start()
	end	= match.end()
	count 	+= 1 	
	#print(match.span())

	output = ("Nobody#:", count, start, end)
	print(output)


