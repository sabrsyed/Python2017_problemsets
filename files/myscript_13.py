#!/usr/bin/env python3

#Python_04 question 

junkset = [101,2,15,22,95,33,2,27,72,15,52]
sum_even = 0
sum_odd = 0 

sorted = sorted(junkset)

for junk in sorted:
	print(junk)
 
for junk in sorted:
	if junk % 2 ==0:
		sum_even += junk

print("sum_even:", sum_even)

for junk in sorted:
        if junk % 2 !=0:
        	sum_odd += junk

print("sum_odd:", sum_odd)
