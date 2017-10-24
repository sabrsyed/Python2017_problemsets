#!/usr/bin/env python3
#Python_06 question 1


import re

poem_read = open ("../Python_06_nobody.txt", "r")
someone = open ("../someone.txt", "w")

poem= poem_read.read()
print(poem)

newpoem = poem.replace('Nobody','Someone')
someone.write(newpoem)

poem_read.close()
someone.close()
