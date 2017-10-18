#!/usr/bin/env python3

#assign a value to a variable

variable1=23

if variable1 % 2 == 0:
	message = "is even"
	print(variable1, message)

elif variable1 > 21:
	message = "is very big"
	print (variable1, message)

elif variable1 < 21:
	message = "is puny"
	print(variable1, message)

else:
	message = "is the same!"
	print(variable1, message)

