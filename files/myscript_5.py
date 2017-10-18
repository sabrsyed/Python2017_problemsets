#!/usr/bin/env python3
import sys

#stuff

variable1 = float(sys.argv[1])

if variable1 ==0:
        message = "is 0"
        print (variable1, message)

elif variable1 < 0:
        message = "is negative"
        print(variable1, message)

elif variable1 > 50 and variable1 % 3 ==0:
        message = "is positive, is greater than 50, and divisible by 3"
        print (variable1, message)

elif variable1 < 50 and variable1 % 2 ==0:
        message = "is positive, is smaller than 50, and is an even number"
        print (variable1, message)

elif variable1 < 50 and variable1 % 2 !=0:
        message = "is positive, is smaller than 50"
        print (variable1, message)

elif variable1 > 50 and variable1 % 3 !=0:
        message = "is positive, is greater than 50"
        print (variable1, message)

elif variable1 ==0:
        message = "is 0"
        print (variable1, message)

else:
	message = "is crap"
	print(variable1, message)



