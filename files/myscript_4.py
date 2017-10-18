#!/usr/bin/env python3
import sys

#Assigns a value to a variable and include an if/else statement

variable1 = float(sys.argv[1])

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
