#!/usr/bin/env python3
#Python_05 question 1

file = open("../python_05.txt", "r")
contents = file.read()
print (contents)

song_upper = contents.upper()
print (song_upper)

file.close()
